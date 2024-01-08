import requests
import xml.etree.ElementTree as ET


def load_xml_file(url: str):
    r = requests.get(url)
    print(f'XML link status: {r.status_code}')
    tree = ET.fromstring(requests.get(url).content)
    return tree


def read_xml():
    pass


if __name__ == "__main__":
    pass
