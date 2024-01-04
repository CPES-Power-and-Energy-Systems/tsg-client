
def parse_resources(ids_message):
    catalogs = ids_message['ids:resourceCatalog']
    data = []

    for catalog in catalogs:
        data.append({'catalog': catalog})

    return
