
import re
import getpass

def password_check(password) :

    strength = 0
    feedback = []

    #length
    if len(password) >= 8:
        strength +=1
    else:
        feedback.append("password length should be at least 8 characters")

    #upper case
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("password should contain at least one uppercase character")

    #lower case
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("password should contain at least one lowercase character")

    #number
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("password should contain at least one digit")
    
    #special
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("password should contain at least one special character")

    #common
    common = ['password', '123456', 'qwerty', 'letmein', 'admin']
    if password.lower() in common:
        score = 0
        feedback.append("no dice. this is a very common password")

    def passwd_strength(score):
        if score >= 8:
            return "strong"
        elif score >= 6:
            return "fairly strong"
        elif score >= 5:
            return "weak"
        else:
            return "outright careless"
        

    #main
    def main():

        while True:
            password = getpass.getpass("enter password: ")

            #user can type exit to exit checker
            if password.lower() == 'exit':
                break

            if not password:
                print("enter a password")
                continue

            score, feedback = password_check(password)
            strength = passwd_strength(score)

            print(f"\nPassword Strength: {strength} ({score}/5)")
            print("Details:")

            if feedback:
                for i in feedback:
                    print(f"  {i}")

            
