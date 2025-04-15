#BMI=weight in kg/(height*height in meters)
def calculatorBMI(weight,height):
    heightinMeters=height*0.3256
    BMI=weight/(heightinMeters*heightinMeters)
    return BMI

print(calculatorBMI(50,5.6))
print(calculatorBMI(75,6.5))