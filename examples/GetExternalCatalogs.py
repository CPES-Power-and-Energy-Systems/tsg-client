"""
external_connector_catalogs.py

This  request retrieves and prints information about external connector catalogs using a
connection to a custom connector. It loads environment variables from a .env file,
establishes a connection to the custom connector, and then retrieves and prints information
about the catalogs from the external connector's self-description.

Usage:
1. Make sure to create a .env file in the parent directory with the following variables:
   - EXTERNAL_CONNECTOR_ID: Custom connector ID for the external connection

2. Import this  request and execute it to print information about external connector catalogs.

Example:
    from external_connector_catalogs import catalogs

    # The 'catalogs' object contains information about external connector catalogs.
    # Print or use this information as needed.

Note:
    Ensure that the required environment variables are set in the .env file before using this  request.

"""
import os
from pprint import pprint
from dotenv import dotenv_values
from examples import ConnectionToOurConnector, GetExternalSelfDescription

# Load environment variables:
config = dotenv_values(os.path.abspath('../../.env'))

# Get the connection and description objects from the pre-established connection module:
conn = ConnectionToOurConnector.conn
description = GetExternalSelfDescription.description

# Get external connector catalogs
catalogs = conn.parse_resource_catalogs(self_description=description)

print("-" * 79)
print(f"> Connector {config['EXTERNAL_CONNECTOR_ID']} Catalogs:")
pprint(catalogs)
