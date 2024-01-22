from typing import List
from typing import Any
from dataclasses import dataclass


@dataclass
class OfferedResource:
    artifact_id: str
    contract_offer: str
    access_url: str

    @staticmethod
    def from_dict(obj: Any) -> 'OfferedResource':
        _access_url = obj['ids:resourceEndpoint'][0]['ids:accessURL']['@id']
        _path = obj['ids:resourceEndpoint'][0]['ids:path']
        access_url = _access_url + _path
        contract_offer = str(obj.get('ids:contractOffer', [''])[0])

        if contract_offer != "":
            artifact_id = obj['ids:representation'][0]['ids:instance'][0]['@id']
        else:
            artifact_id = obj['@id']

        return OfferedResource(artifact_id, contract_offer, access_url)


@dataclass
class ResourceCatalog:
    id: str
    offeredResource: List[OfferedResource]

    @staticmethod
    def from_dict(obj: Any) -> 'ResourceCatalog':
        _id = str(obj.get("@id"))
        _offeredResource = [OfferedResource.from_dict(y) for y in obj.get("ids:offeredResource")]
        return ResourceCatalog(_id, _offeredResource)


@dataclass(frozen=True)
class SelfDescription:
    id: str
    title: str
    description: str
    securityProfile: str
    curator: str
    maintainer: str
    endpoints: str
    catalogs: List['ResourceCatalog']

    @staticmethod
    def from_dict(obj: Any) -> 'SelfDescription':
        """

        :rtype: object
        """
        try:
            _id = str(obj.get("@id"))
            _title = str(obj.get("ids:title")[0].get("@value"))
            _description = str(obj.get("ids:description")[0].get("@value"))
            _security_profile = str(obj.get("ids:securityProfile").get("@id"))
            _curator = str(obj.get("ids:curator").get("@id"))
            _maintainer = str(obj.get("ids:maintainer").get("@id"))
            _endpoints = str(obj.get("ids:hasDefaultEndpoint").get("ids:accessURL").get("@id"))
            _catalogs = [ResourceCatalog.from_dict(y) for y in obj.get("ids:resourceCatalog")]
            return SelfDescription(_id, _title, _description, _security_profile, _curator, _maintainer, _endpoints,
                                   _catalogs)
        except (KeyError, AttributeError, IndexError) as e:
            raise ValueError(f"Error creating SelfDescription: {e}")

    def json(self):
        pass
