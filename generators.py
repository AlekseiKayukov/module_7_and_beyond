def all_variants(text):
    text_length = len(text)

    for i in range(1, text_length + 1):
        for j in range(text_length - i + 1):
            variant = text[j:j + i]
            yield variant

a = all_variants("abc")
for i in a:
    print(i)