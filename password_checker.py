
import re
import getpass

def password_check(password):

    strength = 0
    feedback = []

    #length
    if len(password) >= 8:
        strength +=1
    else:
        feedback.append("password length should be at least 8 characters")

    #upper case
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("password should contain at least one uppercase character")

    #lower case
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("password should contain at least one lowercase character")

    #number
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("password should contain at least one digit")
    
    #special
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("password should contain at least one special character")

    #common
    common = ['password', '123456', 'qwerty', 'letmein', 'admin']
    if password.lower() in common:
        strength = 0
        feedback.append("no dice. this is a very common password")
    
    return strength, feedback

def passwd_strength(strength, password):

    if strength >= 5 and len(password) >10:
        return "strong"
    elif strength >= 4 and len(password) >= 8:
        return "fairly strong"
    elif strength >= 3 and len(password) >= 6:
        return "weak"
    elif strength <3 or len(password) < 6:
        return "outright careless"
        

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

        #user can type exit to exit checker
        if password.lower() == 'exit':
            break

        if not password:
            print("enter a password")
            continue

        strength, feedback = password_check(password)
        strength = passwd_strength(strength, password)

        print(f"\nPassword Strength: {strength}) \nPassword Lenght: {len(password)}")
        print("Details:")

        if feedback:
            for i in feedback:
                print(f"  {i}")
        else:
            print("all checks passed")
        
        if len(password) < 10:
            print("a minimum of 10 characters is adviced")
        
if __name__ == "__main__":
    main()
        
