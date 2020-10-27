my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
all_values = []
for value in my_dict.values():
    all_values.append(value)
all_values.sort()
print(all_values)
print(all_values[-3:])