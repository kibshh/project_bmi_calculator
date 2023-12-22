height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kg: "))

bmi = weight / (height ** 2)

if bmi <= 18.5:
    message = " you are underweight."
elif bmi > 18.5 and bmi <= 25:
    message = " you have a normal weight."
elif bmi > 25 and bmi <= 30:
    message = " you are slightly overweight."
elif bmi > 30 and bmi <= 35:
    message = " you are obese."
else:
    message = " you are clinically obese."

bmi = format(bmi, ".2f")
print(f"Your BMI is {bmi}," + message)