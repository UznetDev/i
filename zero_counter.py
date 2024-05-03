
def zero_count(text: str):
    """
    Matnning boshodagi 0 larning sonini aniqlaydi
    :param text: (string)
    :return: Zero count of front ttext (integer).
    """
    count = 0
    for i in text:
        if i != '0':
            break
        count+=1
    return count


if __name__ == '__main__':
    print('Son yozing men undagi brinchi nollar sonini topib beraman.')
    print(zero_count(input('>>> ')))
