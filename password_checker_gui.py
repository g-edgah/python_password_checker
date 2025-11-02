import tkinter as tk
from tkinter import ttk
import re

class Checker:
    def __init__(self, window):
        self.window = window
        self.ui()

    def ui(self):
        #main frame
        main_frame = ttk.Frame(self.window, padding='20')
        main_frame.pack(fill=tk.BOTH, expand=True)

        #title
        ttk.Label(main_frame, text="password strength checker", font=("Arial", 16, "bold")).pack(pady=10)
       

        #input
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)

        ttk.Label(input_frame, text="password: ").pack(side=tk.LEFT)

        self.password = tk.StringVar()
        self.password_input = ttk.Entry(input_frame, textvariable=self.password, show="*", width=30)
        self.password_input.pack(side=tk.LEFT, padx=10)
        self.password_input.bind("<KeyRelease>", self.realtime_check)

        #hide/show checkbox
        self.checkbox = tk.BooleanVar()
        checkbox_button = ttk.Checkbutton(input_frame, text="show passsword", variable=self.checkbox, command=self.password_visibility)
        checkbox_button.pack(side=tk.LEFT, padx=10)

        #strenght meter
        strength_frame = ttk.LabelFrame(main_frame, text="password strength meter", padding="10")
        strength_frame.pack(fill=tk.X, pady=10)

        self.strength_label = ttk.Label(strength_frame, text="enter password to check")
        self.strength_label.pack()

        #progress bar
        self.progress = ttk.Progressbar(strength_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.progress.pack(pady=5)

        #details
        details_frame = ttk.LabelFrame(main_frame, text='Requirements', padding="10")
        details_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        #requirements
        self.requirements = {
            "lenght": ttk.Label(details_frame, text="at least 10 characters"),
            "uppercase": ttk.Label(details_frame, text="uppercase letter(s)[A-Z]"),
            "lowercase": ttk.Label(details_frame, text="lowercase letter(s) [a-z]"),
            "digit": ttk.Label(details_frame, text="digit(s) [0-9]"),
            "special": ttk.Label(details_frame, text="special character(s) [!@#$...]")
        }

        for req in self.requirements.values():
            req.pack(anchor=tk.W)

        #buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="close", command=self.window.destroy).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="clear", command=self.clear_input).pack(side=tk.LEFT, padx=5)

    def password_visibility(self):
        if self.checkbox.get():
            self.password_input.config(show="")
        else:
            self.password_input.config(show="*")

    def realtime_check(self, password):
        password = self.password.get()
        if password:
            score, feedback =self.strength_check(password)
            self.update_ui(score, feedback, password)
        else:
            self.reset_ui()

    def strength_check(self, password):
        score = 0
        feedback = {}
        length = len(password)

        #lenght
        if length >= 10:
            score += 1
            feedback["lenght"] = True
        else:
            feedback["lenght"] = False

        #uppercase
        if bool(re.search(r'[A-Z]', password)):
            score += 1
            feedback["uppercase"] = True
        else: 
            feedback["uppercase"] = False

        #lowercase
        if bool(re.search(r'[a-z]', password)):
            score += 1
            feedback["lowercase"] = True
        else: 
            feedback["lowercase"] = False

        #digit
        if bool(re.search(r'[0-9]', password)):
            score += 1
            feedback["digit"] = True
        else: 
            feedback["digit"] = False
        
        #special
        if bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
            score += 1
            feedback["special"] = True
        else: 
            feedback["special"] = False

        return score, feedback
    
    def update_ui(self, score, feedback, password):
        
        length = len(password)

        #progress bar
        self.progress['value'] = (score / 5) * 100

        #comment
        if score >=4 and length >=15:
            self.strength_label.config(text = "chef's kiss", foreground="green")
        elif score >=3 and length >= 10:
            self.strength_label.config(text = "this will do", foreground="blue")
        elif score >= 3 and length >=8:
            self.strength_label.config(text = "meeehh. we dont want to be average, do we?", foreground="orange")
        elif score >2 and length >= 6:
            self.strength_label.config(text = "come on", foreground="red")
        elif score <= 2 or  length < 6:
            self.strength_label.config(text = "attrocious! you can surely do better", foreground="red")

        
        #requirements
        for req_name, label in self.requirements.items():
            if feedback[req_name]:
                label.config(foreground="green")
            else:
                label.config( foreground="red")

    def reset_ui(self):
        self.progress['value'] = 0
        self.strength_label.config(text="enter a password to be checked", foreground="black")
        for label in self.requirements.values():
            label.config(foreground="red")
    
    def clear_input(self):
        self.password.set("")
        self.reset_ui()

def main():
    window = tk.Tk()
    window.title("password strength checker")
    window.geometry("525x450")

    Checker(window)

    window.mainloop()

main()