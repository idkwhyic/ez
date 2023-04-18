import random

user_input = input("Enter a string: ").lower()

small_caps_dict = {
    'a': 'ᴀ',
    'b': 'ʙ',
    'c': 'ᴄ',
    'd': 'ᴅ',
    'e': 'ᴇ',
    'f': 'ғ',
    'g': 'ɢ',
    'h': 'ʜ',
    'i': 'ɪ',
    'j': 'ᴊ',
    'k': 'ᴋ',
    'l': 'ʟ',
    'm': 'ᴍ',
    'n': 'ɴ',
    'o': 'ᴏ',
    'p': 'ᴘ',
    'q': 'ǫ',
    'r': 'ʀ',
    's': 's',
    't': 'ᴛ',
    'u': 'ᴜ',
    'v': 'ᴠ',
    'w': 'ᴡ',
    'x': 'x',
    'y': 'ʏ',
    'z': 'ᴢ',
    '1': '₁',
    '2': '₂',
    '3': '₃',
    '4': '₄',
    '5': '₅',
    '6': '₆',
    '7': '₇',
    '8': '₈',
    '9': '₉',
    '0': '₀'
}

output = ''
for char in user_input:
    if char in small_caps_dict:
        output += small_caps_dict[char]
    else:
        output += char

filename = f"small_caps_output_{random.randint(1, 10000)}.txt"
with open(filename, 'w', encoding='utf-8') as file:
    file.write(output)

print(      )
print(      )
print(      )
print(output)
print(      )
print(      )
print(      )
print(f"Converted string saved to {filename}.")
