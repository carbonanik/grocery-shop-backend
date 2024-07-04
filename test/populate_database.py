import json
import requests


def products_from_json():
    file = open("product.json")
    data = file.read()
    json_data = json.loads(data)
    return json_data


def category_from_json():
    file = open("category.json")
    data = file.read()
    json_data = json.loads(data)
    return json_data


def mix():
    category_list = category_from_json()
    product_list = products_from_json()

    for index, category in enumerate(category_list):
        res = requests.post(
            url="http://127.0.0.1:8000/v1/category",
            json=category
        )
        category_list[index] = res.json()
        print(res.json())

    for index, product in enumerate(product_list):
        product["category_id"] = category_list[index % len(category_list)]["id"]

        res = requests.post(
            url="http://127.0.0.1:8000/v1/product",
            json=product
        )
        product_list[index] = res.json()


mix()
