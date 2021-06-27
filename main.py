from tkinter import *
from tkinter import messagebox
BG_COLOR = "#FFEAC9"
symptoms = []
weight = 16000
height = 2
temp = ""
sp = ""
belly = False
chest = False
head = False
gls = False
sore = False
fever = False
vomit = False
urn = False
bre = False
skin = False
brain = False

def isChecked1():
    global belly
    belly = True

def isChecked2():
    global chest
    chest = True

def isChecked3():
    global head
    head = True

def isChecked4():
    global gls
    gls = True

def isChecked5():
    global sore
    sore = True

def isChecked6():
    global fever
    fever = True

def isChecked7():
    global vomit
    vomit = True

def isChecked8():
    global urn
    urn = True

def isChecked9():
    global bre
    bre = True

def isChecked10():
    global skin
    skin = True

def isChecked11():
    global brain
    brain = True

def submit_form(win):
    win.destroy()
    result()


def next_win1(win, i):
    win.destroy()
    go_next(i)


def result():
    new_win = Tk()
    new_win.title("Virtual Health Assistant")
    new_win.config(padx=50, pady=50, width=500, height=500, bg=BG_COLOR)
    result_label = Label(new_win, text="RESULTS", font=("Palatino Linotype", 30, "bold"), fg="#185ADB", bg=BG_COLOR)
    result_label.grid(row=1, column=0, columnspan=2)
    age_label = Label(new_win, text=f"Your Age: {symptoms[0]} years", font=("Palatino Linotype", 15, "normal"), bg=BG_COLOR, fg="#005792")
    age_label.grid(row=2, column=1)
    bmi_label = Label(new_win, text=f"Your BMI points out to {symptoms[1]}", font=("Palatino Linotype", 15, "normal"), bg=BG_COLOR, fg="#005792")
    bmi_label.grid(row=3, column=1)
    temp_label = Label(new_win, text=f"Your temperature: {symptoms[2]}°F", font=("Palatino Linotype", 15, "normal"), bg=BG_COLOR, fg="#005792")
    temp_label.grid(row=4, column=1)
    sp_label = Label(new_win, text=f"Your SpO2: {symptoms[3]}%", font=("Palatino Linotype", 15, "normal"), bg=BG_COLOR, fg="#005792")
    sp_label.grid(row=5, column=1)
    if float(temp) > 99 or float(sp) < 95 or bre or sore or chest or fever:
        covid_label = Label(new_win, text="Warning! Your symptoms indicate danger of COVID-19. Please visit a doctor urgently!", font=("Palatino Linotype", 15, "bold"), bg=BG_COLOR, fg="red")
        covid_label.grid(row=7, column=1)
    if chest and bre:
        diseases_label = Label(new_win, text="Your symptoms point to: Asthma, Bronchitis or Laryngitis", font=("Palatino Linotype", 15, "bold"), bg=BG_COLOR, fg="#005792")
        diseases_label.grid(row=6, column=1)
    if belly or vomit:
        diseases_label = Label(new_win, text="Your symptoms point to: Food Poisoning, Severe Heartburn or Gastritis",
                               font=("Palatino Linotype", 15, "bold"), bg=BG_COLOR, fg="#005792")
        diseases_label.grid(row=6, column=1)
    if chest and sore:
        diseases_label = Label(new_win, text="Your symptoms point to: Sinus Infection, Pneumonia or Pulmonary Embolus",
                               font=("Palatino Linotype", 15, "bold"), bg=BG_COLOR, fg="#005792")
        diseases_label.grid(row=6, column=1)
    if gls and urn:
        diseases_label = Label(new_win, text="Your symptoms point to: Bladder Infection, Prostatitis(if male), Piles or Vaginitis(if female)",
                               font=("Palatino Linotype", 15, "bold"), bg=BG_COLOR, fg="#005792")
        diseases_label.grid(row=6, column=1)
    if brain and head:
        diseases_label = Label(new_win,
                               text="Your symptoms point to: Normal Headaches (nothing to worry about)",
                               font=("Palatino Linotype", 15, "bold"), bg=BG_COLOR, fg="#005792")
        diseases_label.grid(row=6, column=1)
    if brain and head and fever:
        diseases_label = Label(new_win,
                               text="Your symptoms point to: Brain Injury (please visit a doctor ASAP!)",
                               font=("Palatino Linotype", 15, "bold"), bg=BG_COLOR, fg="#005792")
        diseases_label.grid(row=6, column=1)
    if skin and fever:
        diseases_label = Label(new_win,
                               text="Your symptoms point to: Chicken Pox or Small Pox",
                               font=("Palatino Linotype", 15, "bold"), bg=BG_COLOR, fg="#005792")
        diseases_label.grid(row=6, column=1)

def next_win(win, i, en):
    global symptoms
    global weight
    global height
    global temp
    global sp
    if i == 1:
        age = en.get()
        if age == "":
            messagebox.showinfo(title="Error", message="Please enter the required details before proceeding.")
            win.destroy()
            go_next(0)
        symptoms.append(age)
    elif i == 2:
        height = en.get()
        if height == "":
            messagebox.showinfo(title="Error", message="Please enter the required details before proceeding.")
            win.destroy()
            go_next(1)
    elif i == 3:
        weight = en.get()
        if weight == "":
            messagebox.showinfo(title="Error", message="Please enter the required details before proceeding.")
            win.destroy()
            go_next(2)
    elif i == 4:
        temp = en.get()
        if temp == "":
            messagebox.showinfo(title="Error", message="Please enter the required details before proceeding.")
            win.destroy()
            go_next(3)
        symptoms.append(temp)
    elif i == 5:
        sp = en.get()
        if sp == "":
            messagebox.showinfo(title="Error", message="Please enter the required details before proceeding.")
            win.destroy()
            go_next(4)
        symptoms.append(sp)

    bmi = (float(weight) / (float(height) ** 2)) * 10000
    if len(symptoms) == 1:
        if bmi < 18.5:
            symptoms.append("Underweight")
        elif bmi < 24.9:
            symptoms.append("Normal")
        elif bmi < 29.9:
            symptoms.append("Overweight")
        elif 30 < bmi < 60:
            symptoms.append("Obese")

    win.destroy()
    go_next(i)


def go_next(j):
    if j == 0:
        text = "age"
    elif j == 1:
        text = "height (in cm)"
    elif j == 2:
        text = "weight (in kg)"
    elif j == 3:
        text = "temperature (in °F)"
    elif j == 4:
        text = "SpO2"
    elif j == 5:
        text = "blood pressure (in x/y format)"

    new_win = Tk()
    new_win.title("Virtual Health Assistant")
    new_win.config(padx=50, pady=20, width=500, height=500, bg=BG_COLOR)

    nurse_image = PhotoImage(file="nurse.png")
    canvas = Canvas(height=292, width=552, highlightthickness=0, bg=BG_COLOR)
    canvas.create_image(100, 120, image=nurse_image)
    canvas.grid(row=0, column=1)

    welcome_label = Label(new_win, text="Welcome to the Virtual Health Assistant!", font=("Palatino Linotype", 28, "bold"),
                          fg="black", bg=BG_COLOR)
    welcome_label.grid(row=1, column=0, columnspan=2)

    check_label = Label(new_win, text="This interactive tool will check for diseases based on the symptoms that you are facing.",
                        font=("Malgun Gothic", 18, "normal"), bg=BG_COLOR, pady=20, fg="black")
    check_label.grid(row=2, column=0, columnspan=2)
    if j < 5:
        new_label = Label(new_win, text=f"Enter your {text}:", font=("Palatino Linotype", 16, "normal"), bg=BG_COLOR, fg="black")
        new_label.grid(row=3, column=0)
        entry = Entry(new_win, width=52)
        entry.grid(row=3, column=1, columnspan=1, pady=50, ipady=5)
        entry.focus()
        next_button = Button(new_win, text="Next", command=lambda: next_win(new_win, j, entry), width=30)
        next_button.place(relx=0.5, rely=1, anchor=CENTER)
    elif j == 5:
        new_label = Label(new_win, text=f"Enter your {text}:", font=("Palatino Linotype", 16, "normal"), bg=BG_COLOR, fg="black")
        new_label.grid(row=3, column=0)
        entry = Entry(new_win, width=52)
        entry.grid(row=3, column=1, columnspan=1, pady=50, ipady=5)
        entry.focus()
        next_button = Button(new_win, text="Next", command=lambda: next_win1(new_win, j), width=30)
        next_button.place(relx=0.5, rely=1, anchor=CENTER)
    elif j == 6:
        button1 = IntVar()
        button2 = IntVar()
        button3 = IntVar()
        button4 = IntVar()
        new_label = Label(new_win, text=f"Major Pain in:", font=("Palatino Linotype", 16, "normal"), bg=BG_COLOR, fg="black")
        new_label.grid(row=3, column=0)
        pain_button1 = Checkbutton(new_win, text="Belly/Abdomen", onvalue=1, offvalue=0, variable=button1, bg=BG_COLOR, command=isChecked1, font=("Palatino Linotype", 14, "normal"), fg="black", pady=10)
        pain_button1.grid(row=3, column=1)
        symptom_button2 = Checkbutton(new_win, text="Chest", onvalue=1, offvalue=0, variable=button2, bg=BG_COLOR, command=isChecked2, font=("Palatino Linotype", 14, "normal"), fg="black", pady=10)
        symptom_button2.grid(row=4, column=1)
        symptom_button3 = Checkbutton(new_win, text="Head", onvalue=1, offvalue=0, variable=button3, bg=BG_COLOR, command=isChecked3, font=("Palatino Linotype", 14, "normal"), fg="black", pady=10)
        symptom_button3.grid(row=5, column=1)
        symptom_button4 = Checkbutton(new_win, text="Genitals", onvalue=1, offvalue=0, variable=button4, bg=BG_COLOR, command=isChecked4, font=("Palatino Linotype", 14, "normal"), fg="black", pady=10)
        symptom_button4.grid(row=6, column=1)
        next_button = Button(new_win, text="Next", command=lambda: next_win1(new_win, j), width=30)
        next_button.place(relx=0.5, rely=1, anchor=CENTER)
    elif j == 7:
        sym_button1 = IntVar()
        sym_button2 = IntVar()
        sym_button3 = IntVar()
        sym_button4 = IntVar()
        sym_button5 = IntVar()
        sym_button6 = IntVar()
        sym_button7 = IntVar()
        new_label = Label(new_win, text=f"Other Symptoms Include:", font=("Palatino Linotype", 16, "normal"), bg=BG_COLOR, fg="black")
        new_label.grid(row=3, column=0)
        symptom_button1 = Checkbutton(new_win, text="Sore Throat/Cough", onvalue=1, offvalue=0, variable=sym_button1, bg=BG_COLOR,
                                   command=isChecked5, font=("Palatino Linotype", 10, "normal"), fg="black")
        symptom_button1.grid(row=3, column=1)
        symptom_button2 = Checkbutton(new_win, text="Fever", onvalue=1, offvalue=0, variable=sym_button2, bg=BG_COLOR,
                                   command=isChecked6, font=("Palatino Linotype", 10, "normal"), fg="black")
        symptom_button2.grid(row=4, column=1)
        symptom_button3 = Checkbutton(new_win, text="Vomiting", onvalue=1, offvalue=0, variable=sym_button3, bg=BG_COLOR,
                                   command=isChecked7, font=("Palatino Linotype", 10, "normal"), fg="black")
        symptom_button3.grid(row=5, column=1)
        symptom_button4 = Checkbutton(new_win, text="Urine/Stool Related Issues", onvalue=1, offvalue=0, variable=sym_button4, bg=BG_COLOR,
                                   command=isChecked8, font=("Palatino Linotype", 10, "normal"), fg="black")
        symptom_button4.grid(row=6, column=1)
        symptom_button5 = Checkbutton(new_win, text="Breathing Problems", onvalue=1, offvalue=0,
                                      variable=sym_button5, bg=BG_COLOR,
                                      command=isChecked9, font=("Palatino Linotype", 10, "normal"), fg="black")
        symptom_button5.grid(row=7, column=1)
        symptom_button6 = Checkbutton(new_win, text="Skin Problems", onvalue=1, offvalue=0,
                                      variable=sym_button6, bg=BG_COLOR,
                                      command=isChecked10, font=("Palatino Linotype", 10, "normal"), fg="black")
        symptom_button6.grid(row=8, column=1)
        symptom_button7 = Checkbutton(new_win, text="Dizziness/Numbness", onvalue=1, offvalue=0,
                                      variable=sym_button7, bg=BG_COLOR,
                                      command=isChecked11, font=("Palatino Linotype", 10, "normal"), fg="black")
        symptom_button7.grid(row=9, column=1)
        submit_button = Button(new_win, text="Submit", command=lambda: submit_form(new_win))
        submit_button.place(relx=0.5, rely=1, anchor=CENTER)

    j += 1
    new_win.mainloop()


go_next(0)
