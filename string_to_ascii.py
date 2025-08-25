def string_to_ascii(text):
    return ' '.join(str(ord(c)) for c in text)

text = "[YOUR STRING]"
ascii_codes = string_to_ascii(text)
print(ascii_codes)
