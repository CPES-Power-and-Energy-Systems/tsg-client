import os

from tsg_client.controllers.RequestController import RequestController
from tsg_client.controllers.Endpoints import Endpoints
from tsg_client.controllers.SelfDescription import SelfDescription
from utils.file_handling import save_text_file, save_pdf_file, save_csv_file


class TSGController:
    def __init__(self, api_key, connector_id, access_url, agent_id=None):
        self.api_key = api_key
        self.connector_id = connector_id
        self.access_url = access_url
        self.agent_id = agent_id

        # Start inter-connector http requests controller:
        self.endpoints = Endpoints()
        self.controller = RequestController(base_url=self.access_url,
                                            connector_id=self.connector_id,
                                            agent_id=self.agent_id,
                                            api_key=self.api_key)

        self.__validate_connection()

    def __validate_connection(self):
        # Check if the inter-connector API is available and reachable with
        # this API_KEY and ACCESS_URL.
        self.controller.get(endpoint=self.endpoints.RESOURCES,
                            expected_status_code=200)

    def list_dataspace_connectors(self):
        """
        Query the metadata broker to list available connectors by other
        participants in the data space.
        """
        # todo: query metadatabroker & return list of available connectors
        #  in this data space

    def get_connector_selfdescription(self,
                                      connector_id,
                                      access_url,
                                      agent_id=''):
        """
        Get self-descriptions from a connector from another dataspace
        participant, given its connector CONNECTOR_ID and ACCESS_URL.
        """
        params = {
            "connectorId": connector_id,
            "accessUrl": access_url,
            "agentId": agent_id
        }
        rsp = self.controller.get(endpoint=self.endpoints.DESCRIPTION,
                                  params=params,
                                  expected_status_code=200)
        try:
            selfdescription = SelfDescription.from_dict(rsp.json())
            print("SelfDescription object created successfully.")
        except ValueError as ve:
            selfdescription = "error"
            print(f"Error creating SelfDescription: {ve}")

        # todo: it should be possible to perform this request without the
        #  access url being specified (i.e., the Metadata Broker should provide
        #  this info given the connector ID) -- confirm

        return selfdescription

    @staticmethod
    def parse_resource_catalogs(self_description):
        return self_description.catalogs

    @staticmethod
    def parse_catalog_artifacts(self_description):
        artifacts = []
        if self_description.catalogs:
            for catalog in self_description.catalogs:
                for resource in catalog.offeredResource:
                    artifacts.append(
                        {
                            "id": resource.artifact_id,
                            "contract_offer": resource.contract_offer,
                            "access_url": resource.access_url,
                        }
                    )

        return artifacts

    def request_agreement(self, connector_id, artifact_access_url, artifact_contract_offer):
        """
        Request Contract Agreement for a data artifact from another connector,
        """
        payload = {
            "connectorId": connector_id,
            "agentId": '',
            "contractOffer": artifact_contract_offer,
            "accessUrl": artifact_access_url
        }

        rsp = self.controller.post(endpoint=self.endpoints.CONTRACT_REQUEST,
                                   data=payload,
                                   files={'a': 'a'})

        return rsp.json()['@id']

    def request_data_artifact(self, artifact_id, artifact_access_url,
                              connector_id, agent_id, contract_agreement_id, keep_original_format):
        """
        Request a data artifact from another connector, given the artifact ACCESS_URL.
        """

        params = {
            "artifact": artifact_id,
            "connectorId": connector_id,
            "agentId": agent_id,
            "accessUrl": artifact_access_url,
            "transferContract": contract_agreement_id,
        }
        rsp = self.controller.get(endpoint=self.endpoints.ARTIFACTS_CONSUMER,
                                  params=params)

        # Remove spaces & special characters from artifact_id
        artifact_id = artifact_id.strip().replace(':', '_')

        if not keep_original_format:
            txt_filename = f"{artifact_id}.txt"
            txt_path = os.path.join(os.getcwd(), txt_filename)
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(rsp.text)
            return {"message": f"Text file saved to {txt_path}"}

        content_type = rsp.headers.get('content-type')
        if content_type == 'application/json':
            return save_text_file(artifact_id, rsp.text)
        elif content_type == 'application/pdf':
            return save_pdf_file(artifact_id, rsp.content)
        elif content_type == 'text/csv':
            return save_csv_file(artifact_id, rsp.text)
        else:
            return {"message": "Unsupported format"}

    def publish_data_artifact(self, artifact, title,
                              description,
                              contract_offer):
        """
        Publish a data artifact for this connector
        """
        payload = {
            "artifact": artifact,
            "title": title,
            "description": description,
            "contractOffer": contract_offer
        }

        rsp = self.controller.post(endpoint=self.endpoints.ARTIFACTS_PROVIDER,
                                   data=payload,
                                   files=payload)
        return rsp.json()

    def get_connector_self_selfdescription(self):

        rsp = self.controller.get(endpoint=self.endpoints.SELF_DESCRIPTION,
                                  expected_status_code=200)
        try:
            self_description = SelfDescription.from_dict(rsp.json())
            print("SelfDescription object created successfully.")
        except ValueError as ve:
            self_description = "error"
            print(f"Error creating SelfDescription: {ve}")

        return self_description

    def get_openapi_specs(self, external_self_description, api_version):

        connector_id = external_self_description.id
        resource_catalog = external_self_description.catalogs

        endpoint_documentation_urls = []
        for resource in resource_catalog:
            if resource.id == (connector_id + ':data-app'):

                offered_resource = resource.offeredResource

                for off_res in offered_resource:
                    if off_res.path[-len(api_version):] == api_version:
                        endpoint_documentation_urls.append(off_res.documentation)

        return endpoint_documentation_urls

    def openapi_request(self, external_accessURL, external_connector_id, api_version, endpoint, params=""):

        headers = {
            'Forward-AccessURL': external_accessURL,
            'Forward-Sender': self.agent_id,
            'Forward-To': external_connector_id,
            'Forward-Recipient': external_connector_id
        }

        full_endpoint = self.endpoints.OPEN_API + '/' + api_version + '/' + endpoint + '/?' + params

        rsp = self.controller.get(endpoint=full_endpoint, headers=headers)
        return rsp.json()
