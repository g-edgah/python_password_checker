import string
import getpass

password = "helloworld1"

score = 0

conditions = ["ascii_uppercase", "ascii_lowercase", "punctuation", "digits"]

def character_variety(password):
    for i in conditions:
        exists =  any([1 if c in getattr(string, i) else 0 for c in password])

        if exists:
            score += 1

#importing a dictionary of common passwords
with open("common_passwds.txt", "r") as f:
    common = f.read().splitlines()

if password in common:
    print ("this is a very common password")
    strength = 0

def strength(password):
    length = len(password)

    if score >=4 and length >=15:
        return "chef's kiss"
    elif score >=3 and length >= 10:
        return "this will do"
    elif score >= 3 and length >=8:
        return "meeehh. we dont want to be average, do we?"
    elif score <3 and length >= 6:
        return "come on"
    elif score < 3 or  length < 6:
        return "eeiiii! attrocious! you can surely do better"




def passwd_strength(strength, password):

    if strength >= 5 and len(password) >10:
        return "strong"
    elif strength >= 4 and len(password) >= 8:
        return "fairly strong"
    elif strength >= 2 and len(password) >= 6:
        return "weak"
    elif strength <5 or len(password) < 6:
        return "outright careless"

 #main
def main():

    while True:

        mode = 'show'
        print ("type 'hide' to hide password as you type and 'show' to show password as you type")

        def hide_show(mode):
            if mode.lower() == 'hide':
                return getpass.getpass("enter password(hidden): ")
            elif mode.lower() == 'show':
               return input("enter password(visible): ")
        
        password = hide_show('show')
       
        if password == 'show' or password == 'hide':
            hide_show(password)
        elif password.lower() == 'exit':
            break
        elif not password:
            print("enter a password")
            continue
        else:
            print(f"\nPassword Strength: {strength}) \nPassword Lenght: {len(password)}")
            print("Details:")
            
            if len(password) < 10:
                print("a minimum of 10 characters is adviced")
        
main()