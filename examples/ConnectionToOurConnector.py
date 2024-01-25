"""
tsg_connector_setup.py

This  request sets up the TSG connector by loading environment variables from a .env file
and initializing a TSGController instance with the provided API key, connector ID,
access URL, and agent ID.

Usage:
1. Make sure to create a .env file in the parent directory with the following variables:
   - API_KEY: Your TSG connector API key
   - CONNECTOR_ID: Your TSG connector ID
   - ACCESS_URL: Your TSG connector access URL
   - AGENT_ID: Your TSG connector agent ID

2. Import this  request and use the 'conn' variable to interact with the TSG connector.

Example:
    from tsg_connector_setup import conn

    # Use the 'conn' object to perform TSG connector operations.

Note:
    Ensure that the required environment variables are set in the .env file before using this  request.

"""
import os

from dotenv import dotenv_values
from tsg_client.controllers import TSGController

config = dotenv_values(os.path.abspath('../../.env'))

# Connect to our TSG connector:
conn = TSGController(api_key=config['API_KEY'],
                     connector_id=config['CONNECTOR_ID'],
                     access_url=config['ACCESS_URL'],
                     agent_id=config['AGENT_ID'])
