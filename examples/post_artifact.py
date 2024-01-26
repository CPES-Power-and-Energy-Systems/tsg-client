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
import os
from dotenv import dotenv_values
from tsg_client.controllers import TSGController


def load_environment_variables():
    """
    Load environment variables from the specified '.env' file.
    """
    return dotenv_values(os.path.abspath('../.env'))


def connect_to_tsg_connector(api_key, connector_id, access_url, agent_id):
    """
    Connect to the TSG (Third-Party System) connector using the provided API key, connector ID, access URL,
    and agent ID.
    """
    return TSGController(api_key=api_key, connector_id=connector_id, access_url=access_url, agent_id=agent_id)


def post_artifact_to_connector(conn, artifact_path, contract_offer_content, artifact_description, artifact_title):
    """
    Post artifact on the TSG connector.

    Parameters:
    - conn: TSG connector instance.
    - artifact_path: Path to the artifact.
    - contract_offer_content: Content of the contract offer.
    - artifact_description: Description of the artifact.
    - artifact_title: Title of the artifact.

    Returns:
    - Data artifact information.
    """
    return conn.publish_data_artifact(
        artifact=artifact_path,
        contract_offer=contract_offer_content,
        description=artifact_description,
        title=artifact_title
    )


if __name__ == "__main__":
    # Load environment variables:
    config = load_environment_variables()

    # Connect to our TSG connector:
    conn = connect_to_tsg_connector(
        api_key=config['API_KEY'],
        connector_id=config['CONNECTOR_ID'],
        access_url=config['ACCESS_URL'],
        agent_id=config['AGENT_ID']
    )

    # Specify the required parameters:
    artifact_path = "<artifact_path>"
    artifact_description = "<description>"
    artifact_title = "<title>"
    contract_offer_path = "../files/contracts/default.json"

    # Read the contract offer content from the file:
    with open(contract_offer_path, 'r') as file:
        contract_offer_content = file.read()

    # Post artifact on our connector:
    data_artifact = post_artifact_to_connector(
        conn=conn,
        artifact_path=artifact_path,
        contract_offer_content=contract_offer_content,
        artifact_description=artifact_description,
        artifact_title=artifact_title
    )

    print(data_artifact)
