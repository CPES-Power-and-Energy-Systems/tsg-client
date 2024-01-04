
from tsg_client.controllers.RequestController import RequestController
from tsg_client.controllers.Endpoints import Endpoints


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

        # todo: @Carolina validate if the response is a valid self-description
        #  it might happen that the response SC is 200 and the payload is not
        #  as expected (e.g., try to remove /selfdescription from
        #  the access_url)

        # todo: it should be possible to perform this request without the
        #  access url being specified (i.e., the Metadata Broker should provide
        #  this info given the connector ID) -- confirm

        return rsp.json()

    @staticmethod
    def parse_resource_catalogs(self_description):
        # method to extract relevant information from self-description catalog
        # namely, the available catalogs and their artifacts
        # can be split in two methods - Data resources & Data Apps
        # todo: to be improved - just retrieve relevant info
        return self_description['ids:resourceCatalog']

    @staticmethod
    def parse_catalog_artifacts(self_description):
        # method to extract relevant information from self-description catalog
        # namely, the available catalogs and their artifacts
        # can be split in two methods - Data resources & Data Apps
        # todo: to be improved - just retrieve relevant info
        catalogs = self_description['ids:resourceCatalog']

        artifacts = []
        for catalog in catalogs:
            for resource in catalog['ids:offeredResource']:
                _access_url = resource['ids:resourceEndpoint'][0]['ids:accessURL']['@id']
                _path = resource['ids:resourceEndpoint'][0]['ids:path']
                access_url = _access_url + _path
                contract_offer = str(resource.get('ids:contractOffer', [''])[0])

                if contract_offer != "":
                    artifact_id = resource['ids:representation'][0]['ids:instance'][0]['@id']
                else:
                    artifact_id = resource['@id']

                artifacts.append(
                    {
                        "id": artifact_id,
                        "contract_offer": contract_offer,
                        "access_url": access_url,
                    }
                )

        return artifacts

    def request_agreement(self, artifact_access_url, artifact_contract_offer):
        """
        Request Contract Agreement for a data artifact from another connector,
        """
        # todo: check why it breaks when connectorId is specified
        payload = {
            'connectorId': '',
            'agentId': '',
            "contractOffer": artifact_contract_offer,
            "accessUrl": artifact_access_url
        }

        rsp = self.controller.post(endpoint=self.endpoints.CONTRACT_REQUEST,
                                   data=payload,
                                   files={'a': 'a'})

        return rsp.json()['@id']

    def request_data_artifact(self, artifact_id, artifact_access_url,
                              connector_id, agent_id, contract_agreement_id):
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
        # todo: maybe add a parser to return a specific type of msg
        #  as an artifact may not always be json (e.g., in TNO example is a PDF)
        return rsp

    def publish_data_artifact(self, artifact, title,
                              description,
                              contract_offer):
        """
        Publish a data artifact for this connector
        """
        # todo: complete - check @Vasco example
        pass
