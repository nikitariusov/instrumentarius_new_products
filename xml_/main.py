import requests
import xml.etree.ElementTree as ET
from xls_parameters.main import get_settings
from xml_.classes import Product_item


def load_xml_file(url: str):
    r = requests.get(url)
    print(f'XML link status: {r.status_code}')
    tree = ET.fromstring(requests.get(url).content)
    return tree


def get_attr(elem_to_find, param_name):
    if param_name:
        elem = elem_to_find.find(param_name)
        if elem is None:
            return None
        else:
            return elem.text
    else:
        return None


def read_xml(tree, param):
    offers = []
    items_xml = tree.findall(param.offers)
    for i in items_xml:
        offers.append(Product_item(
            get_attr(i, param.item_available),
            i.get('id'),
            get_attr(i, param.price),
            get_attr(i, param.name),
            get_attr(i, param.descr),
            get_attr(i, param.currency) or "UAH",
            get_attr(i, param.category_id),
            get_attr(i, param.image),
            get_attr(i, param.brand),
        ))
    return offers


if __name__ == "__main__":
    test_param = get_settings()[0]
    test_link = test_param.link
    tree = load_xml_file(test_link)
    print(tree)
    print(test_param.log())

    offers = read_xml(tree, test_param)
    offers[10].log()
