def count_animals(st):
    animals = ["dog", "cat", "bat", "cock", "cow", "pig", "fox", "ant", "bird", "lion", "wolf", "deer", "bear", "frog",
               "hen", "mole", "duck", "goat"]
    count = 0
    for i in animals:
        c = st.count(i)
        count+=c

    text = list(st)

    for i in animals:
        j = list(i)
        ch = True
        for x in j:
            if x not in text:
                ch = False
        if ch:
            count+=1
            for x in j:
                text.remove(x)
    return count



# Test
print(count_animals("goatcode"), ' - ', 2)
print(count_animals("cockdogwdufrbir"), ' - ', 4)
print(count_animals("dogdogdogdogdog"), ' - ', 5)

