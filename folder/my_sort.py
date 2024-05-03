from typing import List


def my_sort(lst: list[int]) -> List[int]:
    return sorted(lst, key=lambda x: eval('+'.join(str(x))))


print(my_sort([5, 31, 123, 80, 11]))