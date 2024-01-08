class Params:
    """Параметры для работы парсера"""
    def __init__(self, company, link, offers, item_available, vendor_code, price, name, descr, currency,
                 category_id, image, available, brand):
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
        self.available = available
        self.brand = brand
