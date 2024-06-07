def all_variants(string_data):

    length = len(string_data)
    for i in range(1, length+1):
        for j in range(length - i + 1):
            yield string_data[j:j+i]

a = all_variants("abc")
for i in a:
    print(i)