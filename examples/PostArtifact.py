"""
publish_data_artifact.py

This  request publishes a data artifact on a custom connector using a connection to the connector.
It uses a pre-established connection from the examples  request to our connector.

Usage:
1. Ensure that the required parameters are specified before executing the  request:
   - artifact_path: The path to the data artifact.
   - artifact_description: The description of the data artifact.
   - artifact_title: The title of the data artifact.
   - contract_offer_path: The path to the contract offer file.

2. Import this  request and execute it to publish the data artifact on the custom connector.

Example:
    from publish_data_artifact import data_artifact

    # The 'data_artifact' object contains information about the published data artifact.
    # Print or use this information as needed.

Note:
    Make sure to provide the required parameters before executing this  request.

"""

from examples import ConnectionToOurConnector

# Get the connection object from the pre-established connection module:
conn = ConnectionToOurConnector.conn

# Specify the required parameters:
artifact_path = "<artifact_path>"
artifact_description = "<description>"
artifact_title = "<title>"
contract_offer_path = "../../files/contracts/default.json"

# Read the contract offer content from the file:
with open(contract_offer_path, 'r') as file:
    contract_offer_content = file.read()

# Post artifact on our connector:
data_artifact = conn.publish_data_artifact(artifact=artifact_path,
                                           contract_offer=contract_offer_content,
                                           description=artifact_description,
                                           title=artifact_title)

print(data_artifact)
