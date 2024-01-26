"""
connector_self_selfdescription.py

This  request retrieves and prints information about an internal connector's self-self-description
using a connection to a custom connector. It uses a pre-established connection from the examples
 request to our connector.

Usage:
1. Import this  request and execute it to print information about the internal connector's self-self-description.

Example:
    from connector_self_selfdescription import self_description

    # The 'self_description' object contains information about the internal connector's self-self-description.
    # Print or use this information as needed.

Note:
    Ensure that the required connection to the custom connector is established before using this  request.

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

    # Get internal connector info (self self-description):
    self_description = conn.get_connector_self_selfdescription()

    print("-" * 79)
    print("> Connector Self Self Description:")
    pprint(self_description)
