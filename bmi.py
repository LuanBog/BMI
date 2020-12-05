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
    try:
        height = int(input("Height (Meters): "))
        weight = int(input("Weight (Kilograms): "))
    except:
        print("Something went wrong! Oops, try again later")
        sys.exit()

    bmi = BMI.calculate(height, weight)
    judge = BMI.judge(bmi)

    print("your bmi is {}, you're {}".format(bmi, judge))
