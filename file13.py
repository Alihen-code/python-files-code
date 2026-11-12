some_text = input("Enter your text:")

if some_text.strip() and all(ch.isalpha() or ch.isspace() for ch in some_text):
    print('the input is a string')
else:
    print('the input is not a string')