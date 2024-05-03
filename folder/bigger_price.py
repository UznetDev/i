from typing import List


def bigger_price(son: int, list: List[dict]) -> List:
    """
    songa mos eng qimmat mahsulotlarni chiqarish.
    :param son: return data count
    :param list: list of product
    :return: berilgan songa mos list (list)
    """
    return sorted(list, key=lambda x: x['price'], reverse=True)[:son]


list = [{"name": "wine", "price": 138},
        {"name": "bread", "price": 100},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}]
print(bigger_price(2, list))