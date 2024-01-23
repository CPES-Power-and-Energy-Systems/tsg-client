# TSG-Client Setup Instructions

This document provides detailed instructions for setting up the TSG-Client environment. Please follow these steps carefully to ensure successful configuration and deployment.


## Overview
TSG Client is a Python library for interacting with the Technical Services Grid (TSG) platform. It provides a simple and easy-to-use interface for tasks such as:

- Connecting to TSG connectors
- Retrieving connector self-descriptions
- Working with catalogs and artifacts
- Requesting and consuming data artifacts


## Installation steps

### Install essential tools


- **Install GIT:**
  - Download and install GIT from [Git Download Page](https://git-scm.com/downloads)

- **Python**: Install Python (tested using Python 3.9)

- **Install Python requirements:**
  - Open a terminal and execute the following command:
    ```bash
    pip install -r requirements.txt
    ```

### Clone the project and setup the environment

Open a terminal and execute the following commands:

```bash
git clone https://gitlab.inesctec.pt/cpes/european-projects/enershare/tsg-client.git
cd tsg-client
```

### Set up environment variables

Create a `.env` file with the following contents:

```bash
cp dotenv .env
```

### Edit the .env file and replace the following placeholders with your specific values:

Open the `.env` file in a text editor and modify the following variables with your actual information:

- **API_KEY**: Replace with your TSG API key.
- **CONNECTOR_ID**: Replace with the connector ID for your TSG instance.
- **ACCESS_URL**: Replace with the access URL for your TSG connector.
- **AGENT_ID**: Replace with the agent ID associated with your TSG connector.

Make sure to save the changes after updating the values.

### Run the main script

```bash
python main.py
```
Follow the on-screen prompts in the terminal to complete the setup.


## Additional Information

The TSG-Client is a REST API that interacts with the connector of the dataspace of TNO, deployed following a specific tutorial. The available requests are currently being tested in `main.py`. The script demonstrates interactions with TSG OpenApi Data APP and inter-connector API.



## Usage

To use the TSG Client, you first need to create a `TSGController` instance:

```bash
from tsg_client.controllers import TSGController

config = {
    "API_KEY": "<YOUR_API_KEY>",
    "CONNECTOR_ID": "<YOUR_CONNECTOR_ID>",
    "ACCESS_URL": "<YOUR_ACCESS_URL>",
    "AGENT_ID": "<YOUR_AGENT_ID>",
}

conn = TSGController(**config)
```

1. Connect to a TSG connector:

    ```bash
    conn.connect()
    ```

2. Get connector self-description:

    ```bash
    self_description = conn.get_connector_self_selfdescription()
    print(self_description)
    ```

3. Get external connector self-description:

    ```bash
    access_url = "https://<external_connector_url>/selfdescription"
    connector_id = "<external_connector_id>"
    agent_id = "<agent_id>"
    
    description = conn.get_connector_selfdescription(
        access_url=access_url,
        connector_id=connector_id,
        agent_id=agent_id
    )
    print(description)

    ```
4. Work with catalogs and artifacts:

    ```bash
    # Parse resource catalogs
    catalogs = conn.parse_resource_catalogs(self_description=description)
    print(catalogs)
    
    # Parse catalog artifacts
    artifacts = conn.parse_catalog_artifacts(self_description=description)
    print(artifacts)
    ```

5. Request and consume data artifacts:
    ```bash
    # Request contract agreement
    artifact_id = artifacts[0]['id']
    artifact_access_url = artifacts[0]['access_url']
    artifact_contract_offer = artifacts[0]['contract_offer']
    
    contract_agreement_id = conn.request_agreement(
        connector_id=external_connector['CONNECTOR_ID'],
        artifact_access_url=artifact_access_url,
        artifact_contract_offer=artifact_contract_offer
    )
    print(contract_agreement_id)
    
    # Request data artifact
    artifact_path = "<artifact_path>"
    artifact_description = "<description>"
    artifact_title = "<title>"
    data_artifact = conn.publish_data_artifact(artifact=artifact_path,
                                               contract_offer=artifacts[0]['contract_offer'],
                                               description=artifact_description,
                                               title=artifact_title)
    
    print(data_artifact)
    ```
      
### Contact Information

If you encounter any issues or have questions, please feel free to reach out to the support team:

- **Carolina Catorze:** [carolina.catorze@inesctec.pt](mailto:carolina.catorze@inesctec.pt)
- **Vasco Maia:** [vasco.r.maia@inesctec.pt](mailto:vasco.r.maia@inesctec.pt)
- **José Ricardo Andrade:** [jose.r.andrade@inesctec.pt](mailto:jose.r.andrade@inesctec.pt)

