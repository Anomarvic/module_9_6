def all_variants(text):
    for k in range(len(text)):
        for i in range(0, len(text) - k):
            yield text[i:i + k + 1]

a = all_variants("abc")
for i in a:
    print(i)

