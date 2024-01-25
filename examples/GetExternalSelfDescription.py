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
from examples import ConnectionToOurConnector

# Load environment variables:
config = dotenv_values(os.path.abspath('../../.env'))

# Get the connection object from the pre-established connection module:
conn = ConnectionToOurConnector.conn

# Get external connector info (self-descriptions):
description = conn.get_connector_selfdescription(
    access_url=config['EXTERNAL_ACCESS_URL'],
    connector_id=config['EXTERNAL_CONNECTOR_ID'],
    agent_id=config['EXTERNAL_AGENT_ID']
)

print("-" * 79)
print(f"> Connector {config['EXTERNAL_CONNECTOR_ID']} Self Description:")
pprint(description)
