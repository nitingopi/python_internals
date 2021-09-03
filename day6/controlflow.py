dict = {10: 10, 12: 30, 13: 40}
for k, v in dict.items():
    print(k, v)


list = [1,4,6,9,10]
for val in list:
    if val%2 == 1:
        continue
    print(val)
