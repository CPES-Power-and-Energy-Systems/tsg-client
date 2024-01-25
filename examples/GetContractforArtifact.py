"""
external_artifact_request.py

This  request requests a contract agreement and retrieves content for an external artifact
using a connection to a custom connector. It loads environment variables from a .env file,
establishes a connection to the custom connector, and then requests a contract agreement
and retrieves content for the first external artifact.

Usage:
1. Make sure to create a .env file in the parent directory with the following variables:
   - EXTERNAL_CONNECTOR_ID: Custom connector ID for the external connection
   - EXTERNAL_AGENT_ID: Agent ID for the external connection

2. Import this  request and execute the external artifact request using the 'artifact_content' variable.

Example:
    from external_artifact_request import artifact_content

    # Use the 'artifact_content' object to access the content of the requested external artifact.

Note:
    Ensure that the required environment variables are set in the .env file before using this  request.

"""
import os

from dotenv import dotenv_values
from examples import ConnectionToOurConnector, GetExternalArtifacts

# Load environment variables:
config = dotenv_values(os.path.abspath('../../.env'))

# Get the connection and artifacts objects from the pre-established connection module:
conn = ConnectionToOurConnector.conn
artifacts = GetExternalArtifacts.artifacts

# Request contract agreement for the first artifact
contract_agreement_id = conn.request_agreement(
    connector_id=config['EXTERNAL_CONNECTOR_ID'],
    artifact_access_url=artifacts[0]['access_url'],
    artifact_contract_offer=artifacts[0]['contract_offer']
)

print("-" * 79)
print(f"> Connector {config['EXTERNAL_CONNECTOR_ID']} Contract {contract_agreement_id}:")

# Retrieve content for the first artifact
artifact_content = conn.request_data_artifact(
    artifact_id=artifacts[0]['id'],
    artifact_access_url=artifacts[0]['access_url'],
    agent_id=config['EXTERNAL_AGENT_ID'],
    connector_id=config['EXTERNAL_CONNECTOR_ID'],
    contract_agreement_id=contract_agreement_id,
    keep_original_format=True,
    file_path=""
)

print(artifact_content)
