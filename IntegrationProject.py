"""__author__ = "Corey Record" """


# Description: This program will be a calorie tracker that will help you either
# lose or gain weight based on your goals.


def main():
    """ Input initial variables """
    print("Welcome to the app that will help you meet your caloric goal!")
    print()
    while True:
        try:
            weight = float(input("What is your starting weight in pounds? "))
        except ValueError:
            print("Please enter an integer.")
            continue
        else:
            break
    while True:
        try:
            height = int(input("What is your height in inches? "))
        except ValueError:
            print("Please enter an integer.")
            continue
        else:
            break
    gender = str(input("What is your gender? male/female "))
    while True:
        if gender == "male":
            break
        elif gender == "female":
            break
        else:
            print("Please enter male or female")
            gender = str(input("What is your gender? male/female "))
    while True:
        try:
            age = int(input("What is your age? "))
        except ValueError:
            print("Please enter an integer.")
            continue
        else:
            break
    goal = str(input("What is your goal? gain/lose/maintain "))
    while True:
        if goal == "gain":
            break
        elif goal == "lose":
            break
        elif goal == "maintain":
            break
        else:
            print("Please enter gain, lose, or maintain")
            goal = str(input("What is your goal? gain/lose/maintain "))
    print()
    bmr = 0

    # run if statement if gender is male
    if gender == "male":
        # calculate basal metabolic rate based on goal
        if goal == "lose":
            bmr = ((10 * weight) + (6.25 * height) - (5 * age)) - 200
        if goal == "maintain":
            bmr = ((10 * weight) + (6.25 * height) - (5 * age))
        if goal == "gain":
            bmr = ((10 * weight) + (6.25 * height) - (5 * age)) + 200

        # run if statement if gender is female
    if gender == "female":
        # calculate basal metabolic rate based on goal
        if goal == "lose":
            bmr = ((10 * weight) + (6.25 * height) - (5 * age) - 161) - 200
        if goal == "maintain":
            bmr = ((10 * weight) + (6.25 * height) - (5 * age) - 161)
        if goal == "gain":
            bmr = ((10 * weight) + (6.25 * height) - (5 * age) - 161) + 200

    print("Daily calorie goal is ", format(bmr, ".0f"), " calories", sep="")
    print()

    # defines how many meals
    while True:
        try:
            meal_count = int(input("How many meals did you eat today? "))
        except ValueError:
            print("Please enter a integer.")
            continue
        else:
            break
    total = 0

    # takes the amount of meals and adds the calories
    for x in range(meal_count):
        while True:
            try:
                meal_cal = int(
                    input("How many calories were in one of your meals? "))
                total += meal_cal
            except ValueError:
                print("Please enter an integer.")
                continue
            else:
                break
    # calculate basal metabolic rate based on goal
    # if total >= (bmr - 100) and total <= (bmr + 100): This is how it would be
    # written in most languages
    if (bmr - 100) <= total <= (bmr + 100):
        print("You have eaten in the calorie goal")
    if total < (bmr - 100):
        print("You have eaten in a calorie deficit")
    if total > (bmr + 100):
        print("You have eaten in a calorie surplus")

    print()

    # defines if cardio is performed
    cardio = str(input("Did you perform cardio? yes/no "))
    calories_burned = 0
    while True:
        if cardio == "yes":
            break
        elif cardio == "no":
            break
        else:
            print("Please enter yes or no")
            cardio = str(input("Did you perform cardio? yes/no "))
    # run if cardio is yes
    while True:
        if cardio == "yes":
            # calculates the calories burned based on type of cardio and how
            # much
            cardio_type = str(input("What type of cardio? run/walk/cycle "))
            if cardio_type == "run":
                miles = float(input("How many miles did you run? "))
                calories_burned = miles * 170
                break
            elif cardio_type == "walk":
                miles = float(input("How many miles did you walk? "))
                calories_burned = miles * 100
                break
            elif cardio_type == "cycle":
                miles = float(input("How many miles did you cycle? "))
                calories_burned = miles * 60
                break
            else:
                print("Please enter run, walk, or cycle")
                # cardio = str(input("Did you perform cardio? yes/no "))
            print("You have burned ", format(calories_burned, ".0f"),
                      " calories.", sep="")

        if cardio == "no":
            print("Consider doing cardio to help with your caloric goals.")
            break

    # run if cardio is no
    # if cardio == "no":

    # print("Consider doing cardio to help with your caloric goals.")

    # determines gender for calculation of ideal body weight and calls the
    # function based on that
    if gender == "male":
        ideal_weight_men = ideal_body_weight_men(height)
        print("The ideal body weight for your height is: ",
              format(ideal_weight_men, ".2f"))

    else:
        ideal_weight_female = ideal_body_weight_female(height)
        print("The ideal body weight for your height is: ",
              format(ideal_weight_female, ".2f"))

        # calculates the ideal body weight for males at a certain height


def ideal_body_weight_men(height):
    """ Creates a function that calculates male Ideal body weight"""
    cm_height = height * 30.48
    return 50 + (0.91 * (cm_height - 1700)) - 300


# calculates the ideal body weight for females at a certain height
def ideal_body_weight_female(height):
    """ Creates a function that calculates female Ideal body weight"""
    cm_height = height * 30.48
    return 45.5 + (0.91 * (cm_height - 1700)) - 300


main()

