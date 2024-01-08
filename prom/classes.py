class ProductProm:
    def __init__(self, id, name, name_ukr, seo, seo_ukr, descr, price, currency,
                 image, available, group_number,
                 product_ID, subsection_ID, group_ID, brand, params=None):
        self.id = id
        self.name = name
        self.name_ukr = name_ukr
        self.seo = seo
        self.seo_ukr = seo_ukr
        self.descr = descr
        self.type_product = "r"
        self.price = price
        self.currency = currency
        self.unit = "шт"
        self.image = image
        self.available = available
        self.group_number = group_number
        self.product_ID = product_ID
        self.subsection_ID = subsection_ID
        self.group_ID = group_ID
        self.brand = brand
        self.params = params


class PromGroup:
    def __init__(self, group_number, group_name, group_name_ukr, group_id, parents_number, parents_id):
        self.group_number = group_number
        self.group_name = group_name
        self.group_name_ukr = group_name_ukr
        self.group_id = group_id
        self.parents_number = parents_number
        self.parents_id = parents_id
