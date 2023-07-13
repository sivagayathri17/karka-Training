num1=float(input("your height in m : "))
num2=int(input("your weight in kg : "))
bmi=num2/(num1**2)
print(f"your BMI is {bmi}")
def categories(bmi):
 if bmi<18.5:
    return("underweight")
 elif bmi>=18.5 and bmi<=24.9:
    return("normal weight")
 elif bmi>=25.0 and bmi<29.9:
    return("overweight")
 elif bmi>=30.0:
    return("obese")
categories(bmi)   
print(f"BMI category : {categories(bmi)}")



