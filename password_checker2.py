import string

password = "helloworld"

strength = 0

conditions = ["ascii_uppercase", "ascii_lowercase", "punctuation", "digits"]

for i in conditions:
    exists =  any([1 if c in getattr(string, i) else 0 for c in password])

    if exists:
        strength += 1


length = len(password)

if length >=15:
    strength += 5
elif length >= 10:
    strength += 3
elif length >=8:
    strength += 2
elif length >= 6:
    strength += 1

#importing a dictionary of common passwords
with open("common_passwds.txt", "r") as f:
    common = f.read().splitlines()

if password in common:
    print ("this is a very common password")
    strength = 0



print (strength)