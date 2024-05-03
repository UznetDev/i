

with open('file.txt', 'r') as f:
    text = f.read().split('\n')
    data: {str: list} = {}
    for i in text:
        try:
            res = i.split()
            if int(res[3]) > 0:
                if data.get(res[4]):
                    data[res[4]] += 1
                else:
                    data[res[4]] = 1
        except Exception as err:
            print(err)

    print(max(data, key=lambda x: data[x]))