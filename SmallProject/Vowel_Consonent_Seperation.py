Vowels={"a","e","i","o","u",}

print('Please Enter a sentence to seperate: \n')
message=input()
vowels_letters=""
consonent_letters=""
for letters in message:
    if letters.lower() in Vowels:
        vowels_letters+=letters
    if letters not in Vowels:
        consonent_letters+=letters

print('The Vowels are :'+vowels_letters+'\n')
print('The Consonetnts are :'+consonent_letters)