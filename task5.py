a = [9, 1, 10, 4, 0, 5, 7]
for i in a:
    item_count = a.count(i)
    if item_count > 1:
        print('not unique')
    else:
        print('unique')
