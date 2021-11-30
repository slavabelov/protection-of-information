offset = int(input("offset: "))
key = input("key: ")
with open("warAndPeace.txt", encoding='utf-8') as text_file:
    result = ''
    for str in text_file:
        result += str

a = ord('а')
alphabet = ''.join([chr(i) for i in range(a,a+32)])
for sym in key:
    alphabet = alphabet.replace(sym, '')
    alphabet = key + alphabet
for i in range(offset):
    alphabet = alphabet[-1] + alphabet[:-1]

text = ''
for symbol in result:
    if symbol.isalpha():
        text += alphabet[(ord(symbol) - 224) %32 ]
    else:
        text += symbol


if __name__ == "__main__":
    print(text)
    print(alphabet)