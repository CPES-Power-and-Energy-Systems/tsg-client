"""
external_openapi_request.py

This  request performs an external OpenAPI request using a connection to a custom connector.
It loads environment variables from a .env file, establishes a connection to the custom
connector, and then executes an OpenAPI request using the specified API version and endpoint.

Usage:
1. Make sure to create a .env file in the parent directory with the following variables:
   - EXTERNAL_ACCESS_URL: External access URL for the custom connector
   - EXTERNAL_CONNECTOR_ID: Custom connector ID for the external connection

2. Import this  request and execute the external OpenAPI request using the 'open_api_specs' variable.

Example:
    from external_openapi_request import open_api_specs

    # Use the 'open_api_specs' object to access the results of the external OpenAPI request.

Note:
    Ensure that the required environment variables are set in the .env file before using this  request.

"""

import os
from pprint import pprint
from dotenv import dotenv_values
from tsg_client.controllers import TSGController

# Load environment variables:
config = dotenv_values(os.path.abspath('../.env'))

# Connect to our TSG connector:
conn = TSGController(api_key=config['API_KEY'],
                     connector_id=config['CONNECTOR_ID'],
                     access_url=config['ACCESS_URL'],
                     agent_id=config['AGENT_ID'])


def perform_external_openapi_request(external_access_url, external_connector_id, api_version, endpoint):
    """
    Perform an external OpenAPI request using a connection to a custom connector.
    """
    return conn.openapi_request(
        external_access_url,
        external_connector_id,
        api_version,
        endpoint
    )


if __name__ == "__main__":
    # Execute external OpenAPI request:
    api_version = "1.0.0"
    endpoint = "test-service"

    open_api_specs = perform_external_openapi_request(
        config['EXTERNAL_ACCESS_URL'],
        config['EXTERNAL_CONNECTOR_ID'],
        api_version,
        endpoint
    )

    print("-" * 79)
    print(f"> Connector {config['EXTERNAL_CONNECTOR_ID']} OPEN_API REQUEST:")
    pprint(open_api_specs)
