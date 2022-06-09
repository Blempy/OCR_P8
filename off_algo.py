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
