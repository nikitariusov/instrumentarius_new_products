class Params:
    """Параметры для работы парсера"""
    def __init__(self, company, link, offers, item_available, vendor_code, price, name, descr, currency,
                 category_id, image, brand):
        self.company = company
        self.link = link
        self.offers = offers
        self.item_available = item_available
        self.vendor_code = vendor_code
        self.price = price
        self.name = name
        self.descr = descr
        self.currency = currency
        self.category_id = category_id
        self.image = image
        self.brand = brand

    def log(self):
        """Для проверки"""
        print(f'company name: {self.company}\n'
              f'link: {self.link}\n'
              f'offers: {self.offers}\n'
              f'item_available: {self.item_available}\n'
              f'vendor_code: {self.vendor_code}\n'
              f'price: {self.price}\n'
              f'name: {self.name}\n'
              f'descr: {self.descr}\n'
              f'currency: {self.currency}\n'
              f'category_id: {self.category_id}\n'
              f'image: {self.image}\n'
              f'brand: {self.brand}\n'
              )
