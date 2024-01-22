from pprint import pprint
from dotenv import dotenv_values

from tsg_client.controllers import TSGController

# Todo (general):
#  - Method to list available connectors in DS (query Metadata Broker)

# Todo (OpenApi Data APP):
#  - Methods to communicate via TSG OpenApi Data APP (create dedicated branch)

# Todo (inter-connector API): - Method to extract information from my connector (initialized in init)
#  self-descriptions (i.e., catalogs, resources, etc) - Check if there are alternative methods to authenticate in
#  connector (e.g., user / pw instead of API key) - Create method to upload artifact to my connector - Create method
#  to initialize / assign resources to a catalog


# Load environment variables:
config = dotenv_values(".env")

# Example of external connector:
external_conn = {
    "CONNECTOR_ID": 'urn:playground:tsg:connectors:TestConnector',
    "ACCESS_URL": 'https://test-connector.playground.dataspac.es/selfdescription',
    "AGENT_ID": 'urn:playground:tsg:TNO'
}

# Connect to our TSG connector:
conn = TSGController(api_key=config['API_KEY'],
                     connector_id=config['CONNECTOR_ID'],
                     access_url=config['ACCESS_URL'],
                     agent_id=config['AGENT_ID'])

# Get internal connector info ( self self-description):
self_description = conn.get_connector_self_selfdescription()

print("-" * 79)
print("> Connector Self Self Description:")
pprint(self_description)

# Get external connector info (self-descriptions):
description = conn.get_connector_selfdescription(
    access_url=external_conn['ACCESS_URL'],
    connector_id=external_conn['CONNECTOR_ID'],
    agent_id=external_conn['AGENT_ID']
)
print("-" * 79)
print(f"> Connector {external_conn['CONNECTOR_ID']} Self Description:")
pprint(description)

# Get external connector catalogs
catalogs = conn.parse_resource_catalogs(self_description=description)
print("-" * 79)
print(f"> Connector {external_conn['CONNECTOR_ID']} Catalogs:")
pprint(catalogs)

# Get external connector artifacts
artifacts = conn.parse_catalog_artifacts(self_description=description)
print("-" * 79)
print(f"> Connector {external_conn['CONNECTOR_ID']} Artifacts:")
pprint(artifacts)

print("-" * 79)
print(f"> Connector {external_conn['CONNECTOR_ID']} Artifact {artifacts[0]['id']}:")

# Request contract agreement for the first artifact
contract_agreement_id = conn.request_agreement(
    connector_id=external_conn['CONNECTOR_ID'],
    artifact_access_url=artifacts[0]['access_url'],
    artifact_contract_offer=artifacts[0]['contract_offer']
)

print("-" * 79)
print(f"> Connector {external_conn['CONNECTOR_ID']} Contract {contract_agreement_id}:")

artifact_content = conn.request_data_artifact(
    artifact_id=artifacts[0]['id'],
    artifact_access_url=artifacts[0]['access_url'],
    agent_id=external_conn['AGENT_ID'],
    connector_id=external_conn['CONNECTOR_ID'],
    contract_agreement_id=contract_agreement_id,
    keep_original_format=True
)

print(artifact_content)

artifact_path = "<artifact_path>"
artifact_description = "<description>"
artifact_title = "<title>"
data_artifact = conn.publish_data_artifact(artifact=artifact_path,
                                           contract_offer=artifacts[0]['contract_offer'],
                                           description=artifact_description,
                                           title=artifact_title)
print(data_artifact)
