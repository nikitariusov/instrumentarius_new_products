class Product_item:
    """Данные товара"""
    def __init__(self, item_available, product_id, price, name, descr, currency,
                 category_id, image, brand):
        self.item_available = item_available
        self.product_id = product_id
        self.price = price
        self.name = name
        self.descr = descr
        self.currency = currency
        self.category_id = category_id
        self.image = image
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
              f'brand: {self.brand}\n'
              )
