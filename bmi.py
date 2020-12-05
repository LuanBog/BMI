import sys

class BMI:
    # 18.5 < underweight
    # 18.5 - 24.9 normal
    # 25 - 29.9 overweight
    # 30 > obese
    
    @staticmethod
    def judge(bmi):
        if bmi < 18.5:
            return "underweight"
        elif bmi >= 18.5 and bmi <= 24.9:
            return "normal"
        elif bmi >= 25 and bmi <= 29.9:
            return "overweight"
        elif bmi >= 30:
            return "obese"

    @staticmethod
    def calculate(height, weight):
        # Height - Meters
        # Weight - Kilograms

        return round(weight / (height ** 2), 1)

if __name__ == "__main__":

    print("")
    print("Body Mass Index Chart:")
    print("< 18.5 = Underweight")
    print("18.5 - 24.9 = Normal")
    print("25 - 29.9 = Overweight")
    print("30 > = Obese")
    print("")

    try:
        height = float(input("Height (Meters): "))
        weight = float(input("Weight (Kilograms): "))
    except Exception as e:
        print("\n\nSomething went wrong! Oops, try again later\n\nError: {}".format(e))
        sys.exit()

    bmi = BMI.calculate(height, weight)
    judge = BMI.judge(bmi)

    print("BMI (Body Mass Index) is {} = {}".format(bmi, judge))
