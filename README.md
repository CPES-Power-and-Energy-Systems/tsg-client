# TSG-Client

[![version](https://img.shields.io/badge/version-0.0.1-blue.svg)]()
[![status](https://img.shields.io/badge/status-dev-brightgreen.svg)]()
[![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)



This document provides detailed instructions for setting up the TSG-Client environment. Please follow these steps carefully to ensure successful configuration and deployment.


## Overview
TSG Client is a Python library for interacting with the TNO Security Gateway (TSG). It provides a simple and easy-to-use interface for tasks such as:

- Connecting to TSG connectors
- Retrieving connector self-descriptions
- Working with catalogs and artifacts
- Requesting and consuming data artifacts
- Knowing what connectors are in the dataspace
- Take advantage of the OpenAPI functionalities



## Additional Information

The TSG-Client is a REST API that interacts with the connector of the dataspace of TNO, deployed following a specific tutorial. The script demonstrates interactions with TSG OpenApi Data APP and inter-connector API.


## Adding dependencies

To add a new dependency, please add it to the `requirements.in` file and run the following command:

```bash
pip-compile requirements.in
```

This will generate a new `requirements.txt` file with the new dependency added.


## Contacts:

If you have any questions regarding this project, please contact the following people:

Developers (SW source code / methodology questions):
- **Carolina Catorze:** [carolina.catorze@inesctec.pt](mailto:carolina.catorze@inesctec.pt)
- **Vasco Maia:** [vasco.r.maia@inesctec.pt](mailto:vasco.r.maia@inesctec.pt)
- **José Luís Rodrigues:** [jose.l.rodrigues@.inesctec.pt](mailto:jose.l.rodrigues@.inesctec.pt)
- **José Ricardo Andrade:** [jose.r.andrade@inesctec.pt](mailto:jose.r.andrade@inesctec.pt)

