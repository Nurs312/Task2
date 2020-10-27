a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for item_in_a in a:
    if item_in_a in b:
        c.append(item_in_a)
        for i in c:
            item_count = c.count(i)
            if item_count > 1:
                c.remove(i)
print(c)