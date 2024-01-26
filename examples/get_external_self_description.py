"""
external_connector_info.py

This  request retrieves and prints information about an external connector's self-description
using a connection to a custom connector. It loads environment variables from a .env file,
establishes a connection to the custom connector, and then retrieves and prints the
self-description information from the external connector.

Usage:
1. Make sure to create a .env file in the parent directory with the following variables:
   - EXTERNAL_ACCESS_URL: External access URL for the custom connector
   - EXTERNAL_CONNECTOR_ID: Custom connector ID for the external connection
   - EXTERNAL_AGENT_ID: Agent ID for the external connection

2. Import this  request and execute it to print information about the external connector's self-description.

Example:
    from external_connector_info import description

    # The 'description' object contains information about the external connector's self-description.
    # Print or use this information as needed.

Note:
    Ensure that the required environment variables are set in the .env file before using this  request.

"""
import os
from pprint import pprint
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

    # Get external connector info (self-descriptions):
    description = conn.get_connector_selfdescription(
        access_url=config['EXTERNAL_ACCESS_URL'],
        connector_id=config['EXTERNAL_CONNECTOR_ID'],
        agent_id=config['EXTERNAL_AGENT_ID']
    )

    print("-" * 79)
    print(f"> Connector {config['EXTERNAL_CONNECTOR_ID']} Self Description:")
    pprint(description)
