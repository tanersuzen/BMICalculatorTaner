from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=200,height=200)
window.config(padx=30,pady=30)


def calculate_bmi():
    weight = my_weight.get()
    height = my_height.get()

    if weight == "" or height == "":
        my_result.config(text="Enter both weight and height!",fg="red")
    else:
        try:
            bmi = float(weight) / (float(height)/100) ** 2
            if bmi < 16:
                my_category = "Severe Thinness"
            elif 16 < bmi <= 17:
                my_category = "Moderate Thinness"
            elif 17 < bmi <= 18.5:
                my_category = "Mild Thinness"
            elif 18.5 < bmi <= 25:
                my_category = "Normal"
            elif 25 < bmi <= 30:
                my_category = "Overweight"
            elif 30 < bmi <= 35:
                my_category = "Obese Class I"
            elif 35 < bmi <= 40:
                my_category = "Obese Class II"
            else:
                my_category = "Obese Class III"
            my_result.config(text=f"Your BMI: {round(bmi,2)}. You are " + my_category,fg="white")
        except:
            my_result.config(text="Enter valid numbers!",fg="red")


my_label_weight = Label(text="Enter your weight (kg)")
my_label_weight.config(fg="white")
my_label_weight.pack()

my_weight = Entry(width=10)
my_weight.pack()

my_label_height = Label(text="Enter your height (cm)")
my_label_height.config(fg="white")
my_label_height.pack()

my_height = Entry(width=10)
my_height.pack()



my_button = Button(text="Submit", command=calculate_bmi)
my_button.config(padx=10, pady=5)
my_button.pack()

my_result = Label()
my_result.pack()




window.mainloop()