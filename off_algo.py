import random
import requests

from CONST import CAT_URL, NUMBER_OF_CAT


class Category:
    def __init__(self):
        self.request_category = requests.get(CAT_URL)
        self.json_category = dict(self.request_category.json())
        self.id_list = []
        self.url_list = []
        self.dict_category = {}

    def get_random_id(self):
        i = 0
        while i < NUMBER_OF_CAT:
            self.id_list.append(random.randint(0, 9999))
            i += 1
        return self.id_list

    def get_url_from_random_id(self):
        i = 0
        while i < NUMBER_OF_CAT:
            self.url_list.append(self.json_category["tags"][self.id_list[i]]["url"])
            i += 1
        return self.url_list

    def make_category_dict(self):
        i = 0
        if len(self.id_list) == len(self.url_list):
            while i < 5:
                self.dict_category[self.id_list[i]] = self.url_list[i]
                i += 1
        return self.dict_category


"""
# Produits dans la categorie : "count"
# Numero de la page : "page"
# Produits par page : "page_size"
# Produits : "products"

Elements à recuperer dans "products" : 
- image_url
- nutriscore_grade / - nutrition_grade_fr
- product_name / - product_name_fr
"""


# cat_object = Category()
# cat_object.get_random_id()
# cat_object.get_url_from_random_id()
# cat_object.make_category_dict()
#
# product_url_list = []
# for i in cat_object.dict_category.values():
#     product_url_list.append(i)

class Product(Category):
    def __init__(self):
        self.request_product = requests.get(Product.dict_category.values())
        self.json_product = self.request_product.json()
