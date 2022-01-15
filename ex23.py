#23 - Strings, Bytes, Char Encodings

# Download https://learnpythonthehardway.org/python3/languages.txt

# Run using: python3 ex23.py utf-8 strict
# Run using: python3 ex23.py big5 replace
# ENCODING = utf-8, big5
# ERRORS = strict, replace


import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)


languages = open("ex23-languages.txt", encoding="utf-8")

main(languages, input_encoding, error)