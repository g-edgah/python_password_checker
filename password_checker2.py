import string
import getpass


def check(password):
    score = 0
    missing = []

    conditions = ["ascii_uppercase", "ascii_lowercase", "punctuation", "digits"]

    for i in conditions:
        exists =  any([1 if c in getattr(string, i) else 0 for c in password])

        if exists:
            score += 1
        if not exists:
            if i == "ascii_uppercase":
                missing.append("uppercase letter(s)(A-Z)")
            elif i == "ascii_lowercase":
                missing.append("lowercase letter(s)(a-z)")
            elif i == "punctuation":
                missing.append(f"special character(s)({string.punctuation})")
            elif i == "digits":
                missing.append("digit(s)(0-9)")


    #importing a dictionary of common passwords
    with open("common_passwds.txt", "r") as f:
        common = f.read().splitlines()

    if password in common:
        print ("this is a very common password")
        score = 0

    return score, missing

def passwd_strength(score, password):
    length = len(password)

    if score >=4 and length >=15:
        return "chef's kiss"
    elif score >=3 and length >= 10:
        return "this will do"
    elif score >= 3 and length >=8:
        return "meeehh. we dont want to be average, do we?"
    elif score >2 and length >= 6:
        return "come on"
    elif score <= 2 or  length < 6:
        return "eeiiii! attrocious! you can surely do better"


#main
def main():
    mod = "show"
    while True:

        print ("type 'hide' to hide password as you type and 'show' to show password as you type or type exit to exit password checker")
        
        #password = hide_show(mod)
        if mod == "show":
            password = input('enter password(visible): ')  
        elif mod == "hide":
            password = getpass.getpass('enter password(hidden): ')
       
        if password.lower() == 'show' or password.lower() == 'hide':
            mod = password.lower()
            continue
        elif password.lower() == 'exit':
            break
        elif not password:
            print("you have not entered a password")
            continue
        else:
            score, missing = check(password)
            print("Details:")
            print(f"Password Strength: {passwd_strength(score, password)}) \nPassword Lenght: {len(password)} \nwhat you're missing: ")
            
            if missing:
                for i in missing:
                    print(f"  {i}")
            else:
                print("all checks passed")

            if len(password) < 10:
                print ("")
                print("a minimum of 10 characters is adviced for a strong password")
                print("")
                print("")
        
main()