def bmi(weight, height):
    Bmi=weight/height**2

    if Bmi <= 18.5:
        return "Underweight"
    elif Bmi <= 25.0:
        return "Normal"
    elif Bmi <= 30.0:
        return "Overweight"
    elif Bmi > 30:
        return "Obese"