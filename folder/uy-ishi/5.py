def step_polindrom(old, num, step=0):
    if str(num) == str(num)[::-1]:
        print(f"{old} => {step} > {num}")
        return step
    return step_polindrom(old, num + int(str(num)[::-1]), step + 1)

print(step_polindrom(78, 78))