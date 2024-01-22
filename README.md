# TSG-Client Setup Instructions

This document provides detailed instructions for setting up the TSG-Client environment. Please follow these steps carefully to ensure successful configuration and deployment.

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
git clone https://github.com/your-username/tsg-client.git
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

### Contact Information

If you encounter any issues or have questions, please feel free to reach out to the support team:

- **Carolina Catorze:** [carolina.catorze@inesctec.pt](mailto:carolina.catorze@inesctec.pt)
- **Vasco Maia:** [vasco.r.maia@inesctec.pt](mailto:vasco.r.maia@inesctec.pt)
- **José Ricardo Andrade:** [jose.r.andrade@inesctec.pt](mailto:jose.r.andrade@inesctec.pt)

