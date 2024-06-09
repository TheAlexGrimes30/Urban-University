def all_variance(text):
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            yield text[start:end]


a = all_variance("abc")
for i in a:
    print(i)
