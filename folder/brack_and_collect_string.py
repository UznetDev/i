import os
from typing import List


def collect_string(file_name: str) -> List:
    """
    Break and collect string
    :param file_name: file path (string)
    :return: collect string list (list)
    """
    if os.path.exists(file_name):
        res = []
        with open(file_name) as f:
            text = f.read()
            if text:
                ln = len(text)
                for i in range(1,ln+1):
                    res.append(text[:i])
                for i in range(ln-1, 0, -1):
                    res.append(text[:i])
                return res
            else:
                raise Exception("File {} is empty".format(file_name))
    else:
        raise Exception("File {} not found".format(file_name))


if __name__ == '__main__':
    print(collect_string("file.text"))