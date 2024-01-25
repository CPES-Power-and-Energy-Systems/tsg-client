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

from pprint import pprint
from examples import ConnectionToOurConnector

# Get the connection object from the pre-established connection module:
conn = ConnectionToOurConnector.conn

# Get internal connector info (self self-description):
self_description = conn.get_connector_self_selfdescription()

print("-" * 79)
print("> Connector Self Self Description:")
pprint(self_description)
