import tkinter
from tkinter import messagebox

#BMI Logic 
#(educational estimate - not a diagnosis)
def adult_bmi_category(BMI, gender):
    if gender == 1: 
        if BMI < 18.5:
            return "Underweight"
        elif BMI < 25:
            return "Healthy weight"
        elif BMI < 30:
            return "Overweight"
        else:
            return "Obese"   
    elif gender == 2:
        if BMI < 18:
            return "Underweight"
        elif BMI < 24:
            return "Healthy weight"
        elif BMI < 29:
            return "Overweight"
        else:
            return "Obese"
    
def child_bmi_category(BMI, age, gender):
    if 2 <= age <= 5:
        if BMI < 14:
            return "Underweight"
        elif BMI < 17:
            return "Healthy weight"
        elif BMI < 18:
            return "Overweight"
        else:
            return "Obese"   
    elif 6 <= age <= 12:
        if BMI < 14.5:
            return "Underweight"
        elif BMI < 19:
            return "Healthy weight"
        elif BMI < 21:
            return "Overweight"
        else:
            return "Obese"
    elif 13 <= age <= 19:
        if gender == 1: 
            if BMI < 18:
                return "Underweight"
            elif BMI < 24:
                return "Healthy weight"
            elif BMI < 27:
                return "Overweight"
            else:
                return "Obese"
        else: 
            if BMI < 17.5:
                return "Underweight"
            elif BMI < 23.5:
                return "Healthy weight"
            elif BMI < 27:
                return "Overweight"
            else:
                return "Obese"

#Button commands
def calculate():
    try:
        age = int(age_entry.get())
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        gender = radio_var.get()
        BMI = round(weight / (height / 100) ** 2, 1)
    except ValueError:
        messagebox.showerror("Error", message="Please enter valid numbers.")
        return
    if not 2 <= age <= 120:
        messagebox.showerror("Error", message="Invalid age. Please try again.")
        return
    if height <= 0:
        messagebox.showerror("Error", message="Invalid height. Please try again.")
        return
    if weight <= 0:
        messagebox.showerror("Error", message="Invalid weight. Please try again.")
        return
    if gender not in (1, 2):
        messagebox.showerror("Error", message="Please select a gender.")
        return
    if age < 20:
        category = child_bmi_category(BMI, age, gender)
        messagebox.showinfo("Result", message=f"Child BMI = {BMI}\n"
                            f"Category: {category}")
    else:
        category = adult_bmi_category(BMI, gender)
        messagebox.showinfo("Result", message=f"Adult BMI = {BMI}\n"
                            f"Category: {category}")

def reset():
    age_entry.delete(0,'end')
    radio_var.set(None)
    height_entry.delete(0,'end')
    weight_entry.delete(0,'end')

#Layout
window = tkinter.Tk()
window.title('BMI calculator')
window.geometry('700x500')

frame = tkinter.Frame(window,width=700,height=400)
frame.pack(pady=120)

radio_var = tkinter.IntVar()
welcome_label = tkinter.Label(frame,text='Body Mass Index (BMI) Calculator',font=('Arial',16))
age_label = tkinter.Label(frame,text='Enter Age (2-120)',font=('Arial',12))
age_entry = tkinter.Entry(frame,font=('Arial',12))
gender_label = tkinter.Label(frame,text='Select Gender',font=('Arial',12))
gender_button1 = tkinter.Radiobutton(frame,text='Male',value=1,variable=radio_var,font=('Arial',12))
gender_button2 = tkinter.Radiobutton(frame,text='Female',value=2,variable=radio_var,font=('Arial',12))
height_label = tkinter.Label(frame,text='Enter Height (cm)',font=('Arial',12))
height_entry = tkinter.Entry(frame,font=('Arial',12))
weight_label = tkinter.Label(frame,text='Enter Weight (kg)',font=('Arial',12))
weight_entry = tkinter.Entry(frame,font=('Arial',12))
calculate_button = tkinter.Button(frame,text='Calculate',font=('Arial',12),command=calculate)
reset_button = tkinter.Button(frame,text='Reset',font=('Arial',12),command=reset)
exit_button = tkinter.Button(frame,text='Exit',font=('Arial',12),command=exit)

#Positioning
welcome_label.grid(column=0,row=0,columnspan=4,pady=15)
age_label.grid(column=0,row=1,pady=5)
age_entry.grid(column=1,row=1,columnspan=3)
gender_label.grid(column=0,row=2)
gender_button1.grid(column=1,row=2)
gender_button2.grid(column=2,row=2)
height_label.grid(column=0,row=3,pady=5)
height_entry.grid(column=1,row=3,columnspan=3)
weight_label.grid(column=0,row=4,pady=10)
weight_entry.grid(column=1,row=4,columnspan=3)
calculate_button.grid(column=0,row=5,pady=5)
reset_button.grid(column=1,row=5)
exit_button.grid(column=2,row=5)

window.mainloop()
