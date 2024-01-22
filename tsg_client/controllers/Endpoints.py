
from dataclasses import dataclass


@dataclass(frozen=True)
class Endpoints:
    SELF_DESCRIPTION = "selfdescription"
    DESCRIPTION = "api/description"
    RESOURCES = "api/resources"
    ARTIFACTS_CONSUMER = "api/artifacts/consumer/artifact"
    ARTIFACTS_PROVIDER = "api/artifacts/provider"
    CONTRACT_REQUEST = "api/artifacts/consumer/contractRequest"

