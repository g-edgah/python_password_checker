import tkinter as tk
from tkinter import ttk
import re

class Checker:
    def __init__(self, window):
        self.window = window
        self.setup_colors()
        self.ui()

    def setup_colors(self):
        self.colors = {
            'bg_primary': '#DBE2E9',
            'bg_secondary': '#C3CAD2',
            'green': "#007848",
            'yellow': '#f39c12',
            'red': "#820000",
            'selected': '#727F91',
            'blue': '#192bc2',
            'text_primary': '#000000',
            'text_secondary': '#bdc3c7'
        }

    def rounded_rectangle(self, canvas, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1+radius, y1,
            x2-radius, y1,
            x2, y1, x2, y1+radius,
            x2, y2-radius, x2, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1, y2, x1, y2-radius,
            x1, y1+radius, x1, y1
        ]
        return canvas.create_polygon(points, smooth=True, **kwargs)

    def ui(self):
        #main canvas
        self.main_canvas = tk.Canvas(self.window, bg=self.colors['bg_primary'], highlightthickness=0)
        self.main_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Create rounded background for main content
        self.rounded_rectangle(self.main_canvas, 10, 10, 515, 540, radius=20, fill=self.colors['bg_secondary'], outline=self.colors['text_primary'])
        
        #title
        title_canvas = tk.Canvas(self.main_canvas, bg=self.colors['bg_secondary'], highlightthickness=0, height=50)
        title_canvas.place(x=25, y=20, width=475, height=50)
        self.rounded_rectangle(title_canvas, 0, 0, 475, 50, radius=15, fill=self.colors['bg_secondary'], outline=self.colors['bg_secondary'])
        title_canvas.create_text(237, 25, text="password strength checker", fill=self.colors['text_primary'], font=("Arial", 14, "bold"))

        #input frame
        input_canvas = tk.Canvas(self.main_canvas, bg=self.colors['bg_secondary'], highlightthickness=0, height=80)
        input_canvas.place(x=25, y=90, width=475, height=80)
        self.rounded_rectangle(input_canvas, 0, 0, 475, 80, radius=15, fill=self.colors['bg_secondary'], outline=self.colors['text_primary'])

        #password label
        tk.Label(input_canvas, text="Password:", bg=self.colors['bg_secondary'], fg=self.colors['text_primary'], font=("Arial", 10)).place(x=20, y=15)

        #password entry
        entry_frame = tk.Frame(input_canvas, bg=self.colors['bg_secondary'])
        entry_frame.place(x=100, y=12, width=200, height=25)
        self.rounded_rectangle(input_canvas, 98, 10, 302, 38, radius=8, fill=self.colors['bg_primary'], outline=self.colors['text_primary'])

        self.password = tk.StringVar()
        self.password_input = tk.Entry(entry_frame, textvariable=self.password, show="*", 
                                      bg=self.colors['bg_primary'], fg=self.colors['text_primary'],
                                      relief='flat', font=("Arial", 10))
        self.password_input.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        self.password_input.bind("<KeyRelease>", self.realtime_check)

        #show password checkbox
        self.checkbox = tk.BooleanVar()
        checkbox = tk.Checkbutton(input_canvas, text="Show Password", variable=self.checkbox, 
                                 command=self.password_visibility, bg=self.colors['bg_secondary'],
                                 fg=self.colors['text_primary'], selectcolor=self.colors['bg_primary'],
                                 activebackground=self.colors['bg_secondary'], activeforeground=self.colors['text_primary'])
        checkbox.place(x=320, y=15)

        #strength meter
        strength_canvas = tk.Canvas(self.main_canvas, bg=self.colors['bg_secondary'], highlightthickness=0, height=100)
        strength_canvas.place(x=25, y=190, width=475, height=100)
        self.rounded_rectangle(strength_canvas, 0, 0, 475, 100, radius=15, 
                              fill=self.colors['bg_secondary'], outline=self.colors['text_primary'])

        #strength label
        strength_canvas.create_text(15, 15, text="Strength Meter:", anchor='w',
                                   fill=self.colors['text_primary'], font=("Arial", 10, "bold"))

        self.strength_label = tk.Label(strength_canvas, text="Enter password to check", 
                                      bg=self.colors['bg_secondary'], fg=self.colors['text_secondary'],
                                      font=("Arial", 9))
        self.strength_label.place(x=20, y=40)

        #custom progress bar background
        self.rounded_rectangle(strength_canvas, 20, 65, 455, 85, radius=10, 
                              fill=self.colors['bg_primary'], outline=self.colors['text_primary'])

        #progress bar
        self.progress = tk.Canvas(strength_canvas, bg=self.colors['bg_primary'], highlightthickness=0,
                                 width=433, height=18)
        self.progress.place(x=21, y=66)
        self.progress_bar = self.rounded_rectangle(self.progress, 0, 0, 0, 18, radius=8, 
                                                  fill=self.colors['bg_secondary'])

        #requirements
        requirements_canvas = tk.Canvas(self.main_canvas, bg=self.colors['bg_secondary'], highlightthickness=0, height=150)
        requirements_canvas.place(x=25, y=310, width=475, height=150)
        self.rounded_rectangle(requirements_canvas, 0, 0, 475, 150, radius=15, 
                              fill=self.colors['bg_secondary'], outline=self.colors['text_primary'])

        # Requirements title
        requirements_canvas.create_text(15, 15, text="Requirements:", anchor='w',
                                      fill=self.colors['text_primary'], font=("Arial", 10, "bold"))

        #requirements labels
        self.requirements = {
            "lenght": tk.Label(requirements_canvas, text="• At least 10 characters", 
                              bg=self.colors['bg_secondary'], fg=self.colors['red'], font=("Arial", 9)),
            "uppercase": tk.Label(requirements_canvas, text="• Uppercase letter(s) [A-Z]", 
                                 bg=self.colors['bg_secondary'], fg=self.colors['red'], font=("Arial", 9)),
            "lowercase": tk.Label(requirements_canvas, text="• Lowercase letter(s) [a-z]", 
                                 bg=self.colors['bg_secondary'], fg=self.colors['red'], font=("Arial", 9)),
            "digit": tk.Label(requirements_canvas, text="• Digit(s) [0-9]", 
                            bg=self.colors['bg_secondary'], fg=self.colors['red'], font=("Arial", 9)),
            "special": tk.Label(requirements_canvas, text="• Special character(s) [!@#$%^&*(),.?\":{}|<>]", 
                               bg=self.colors['bg_secondary'], fg=self.colors['red'], font=("Arial", 9))
        }

        y_pos = 40
        for req in self.requirements.values():
            req.place(x=20, y=y_pos)
            y_pos += 20

        #buttons
        button_canvas = tk.Canvas(self.main_canvas, bg=self.colors['bg_secondary'], highlightthickness=0, height=50)
        button_canvas.place(x=25, y=470, width=475, height=50)

        #close button
        close_btn_canvas = tk.Canvas(button_canvas, bg=self.colors['bg_secondary'], highlightthickness=0, width=100, height=35)
        close_btn_canvas.place(x=150, y=10)
        self.rounded_rectangle(close_btn_canvas, 0, 0, 100, 35, radius=10, 
                              fill=self.colors['red'], outline=self.colors['text_primary'])
        close_btn_canvas.create_text(50, 17, text="Close", fill=self.colors['text_primary'], font=("Arial", 10, "bold"))
        close_btn_canvas.bind("<Button-1>", lambda e: self.window.destroy())

        #clear button
        clear_btn_canvas = tk.Canvas(button_canvas, bg=self.colors['bg_secondary'], highlightthickness=0, width=100, height=35)
        clear_btn_canvas.place(x=270, y=10)
        self.rounded_rectangle(clear_btn_canvas, 0, 0, 100, 35, radius=10, 
                              fill=self.colors['yellow'], outline=self.colors['text_primary'])
        clear_btn_canvas.create_text(50, 17, text="Clear", fill=self.colors['text_primary'], font=("Arial", 10, "bold"))
        clear_btn_canvas.bind("<Button-1>", lambda e: self.clear_input())

    def password_visibility(self):
        if self.checkbox.get():
            self.password_input.config(show="")
        else:
            self.password_input.config(show="*")

    def realtime_check(self, event):
        password = self.password.get()
        if password:
            score, feedback = self.strength_check(password)
            self.update_ui(score, feedback, password)
        else:
            self.reset_ui()

    def strength_check(self, password):
        score = 0
        feedback = {}
        length = len(password)

        #length
        if length >= 10:
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

        # Digit
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
        meter_score = 0

        #comment
        if score == 4 and length >= 15:
            self.strength_label.config(text="Chef's kiss! Perfect password", foreground=self.colors['green'])
            meter_score = 6
        elif score >= 3 and length >= 10:
            self.strength_label.config(text="This will do - Strong password", foreground=self.colors['green'])
            meter_score = 5
        elif score >= 3 and length >= 8:
            self.strength_label.config(text="Meh... we don't want to be average", foreground=self.colors['yellow'])
            meter_score = 4
        elif score >= 2 and length >= 6:
            self.strength_label.config(text="Keep going - try more variety", foreground=self.colors['yellow'])
            meter_score = 3
        elif score >= 1 and length > 5:
            self.strength_label.config(text="Take another look at requirements", foreground=self.colors['red'])
            meter_score = 2
        elif score <= 1 or length <= 5:
            self.strength_label.config(text="Atrocious! You can do better", foreground=self.colors['red'])
            meter_score = 1

        #progress bar
        progress_width = (meter_score / 6) * 433
        self.progress.coords(self.progress_bar, 0, 0, progress_width, 18)
        
        #update progress bar
        if meter_score >= 5:
            self.progress.itemconfig(self.progress_bar, fill=self.colors['green'])
        elif meter_score >= 3:
            self.progress.itemconfig(self.progress_bar, fill=self.colors['yellow'])
        else:
            self.progress.itemconfig(self.progress_bar, fill=self.colors['red'])
        
        #update requirements
        for req_name, label in self.requirements.items():
            if feedback[req_name]:
                label.config(foreground=self.colors['green'])
            else:
                label.config(foreground=self.colors['red'])

    def reset_ui(self):
        self.progress.coords(self.progress_bar, 0, 0, 0, 18)
        self.strength_label.config(text="Enter password to check", foreground=self.colors['text_secondary'])
        for label in self.requirements.values():
            label.config(foreground=self.colors['red'])
    
    def clear_input(self):
        self.password.set("")
        self.reset_ui()

def main():
    window = tk.Tk()
    window.title("Password Strength Checker")
    window.geometry("525x550")
    window.configure(bg='#2c3e50')
    window.resizable(False, False)
    
    Checker(window)
    window.mainloop()

if __name__ == "__main__":
    main()