import requests
import xml.etree.ElementTree as ET
from xls_parameters.main import get_settings
from xml_.classes import Product_item, Categories
from utils.utils import only_integer


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


def get_images(element, xml_param_name):
    """Получаем все картинки"""

    images = []
    img = element.findall(xml_param_name)
    for i in img:
        images.append(i.text)
    return images


def get_params(element, xml_param_name):
    """Получаем все характеристики"""

    param = element.findall(xml_param_name)
    param_list = []
    for i in param:
        if i.get('name') != 'Картинки':
            param_list.append(
                {i.attrib.get('name'): i.text}
            )
    return param_list


def read_xml(tree, param):
    offers = []
    items_xml = tree.findall(param.offers)
    for i in items_xml:
        offers.append(Product_item(
            get_attr(i, param.item_available),
            i.get('id'),
            only_integer(get_attr(i, param.price)),
            get_attr(i, param.name),
            get_attr(i, param.descr),
            get_attr(i, param.currency) or "UAH",
            get_attr(i, param.category_id),
            get_images(i, param.image),
            get_params(i, param.parameters),
            get_attr(i, param.brand),
        ))
    return offers


def get_categories(tree, params):
    categories = []
    all_parent_cats = []
    all_cats = tree.findall(params)

    for i in all_cats:
        parent_cat = i.get('parentId')
        if parent_cat not in all_parent_cats:
            all_parent_cats.append(parent_cat)

    print(all_parent_cats)

    for i in all_cats:
        parent_id = i.get('parentId')
        i_id = i.get('id')
        categories.append(Categories(
            i_id,
            parent_id,
            i.text,
            i_id in all_parent_cats,
        ))

    return categories


if __name__ == "__main__":
    test_param = get_settings()[0]
    test_link = test_param.link
    tree = load_xml_file(test_link)
    # print(tree)
    # print(test_param.log())

    offers = read_xml(tree, test_param)
    # print(len(offers))
    # offers[0].log()
    test_cats_param = "shop/catalog/category"
    categories = get_categories(tree, test_cats_param)
    print(categories[2].log())
