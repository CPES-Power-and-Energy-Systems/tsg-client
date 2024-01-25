from setuptools import setup

setup(
    name='tsg-client',
    version='0.0.1',
    packages=['tsg_client', 'tsg_client.controllers'],
    url='',
    license='',
    author='Carolina Catorze, Vasco Maia, José Luis Rodrigues, José Ricardo Andrade',
    author_email="""
        - carolina.catorze@inesctec.pt
        - vasco.r.maia@inesctec.pt
        - jose.l.rodrigues@inesctec.pt
        - jose.r.andrade@inesctec.pt
    """,
    description='TSG Client is a Python library for interacting with the TNO Security Gateway (TSG). It '
                'provides a simple and easy-to-use interface for tasks such as: Connecting to TSG connectors, '
                'Retrieving connector self-descriptions, Working with catalogs and artifacts, Requesting and '
                'consuming data artifacts, Knowing what connectors are in the dataspace, Take advantage of the '
                'OpenAPI functionalities',
    install_requires=[
        'loguru~=0.7.2',
        'python-dotenv~=1.0.0',
        'requests~=2.31.0',
        'myst-parser~=2.0.0',
        'sphinx~=7.2.6',
        'sphinx-rtd-theme~=2.0.0',
        'flake8',
    ],

)
