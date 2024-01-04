
from dataclasses import dataclass


@dataclass(frozen=True)
class Endpoints:
    DESCRIPTION = "api/description"
    RESOURCES = "api/resources"
    ARTIFACTS_CONSUMER = "api/artifacts/consumer/artifact"
    ARTIFACTS_PROVIDER = "api/artifacts/provider"
    CONTRACT_REQUEST = "api/artifacts/consumer/contractRequest"

