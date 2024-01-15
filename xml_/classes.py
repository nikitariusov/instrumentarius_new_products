class Product_item:
    """Данные товара"""

    def __init__(self, item_available, product_id, price, name, descr, currency,
                 category_id, image, parameters, brand):
        self.item_available = item_available
        self.product_id = product_id
        self.price = price
        self.name = name
        self.descr = descr
        self.currency = currency
        self.category_id = category_id
        self.image = image
        self.parameters = parameters
        self.brand = brand

    def log(self):
        """Для проверки"""
        print(f'name: {self.name}\n'
              f'item_available: {self.item_available}\n'
              f'product_id: {self.product_id}\n'
              f'price: {self.price}\n'
              f'descr: {self.descr}\n'
              f'currency: {self.currency}\n'
              f'category_id: {self.category_id}\n'
              f'image: {self.image}\n'
              f'parameters: {self.parameters}\n'
              f'brand: {self.brand}\n'
              )


class Categories:
    """Категории с хмл ссылки"""

    def __init__(self, id, parent_id, name, is_parent):
        self.id = id
        self.parent_id = parent_id
        self.name = name
        self.is_parent = is_parent

    def log(self):
        print(f'name: {self.name}\n'
              f'id: {self.id}\n'
              f'parent_id: {self.parent_id}\n'
              f'is_parent: {self.is_parent}\n'
              )
