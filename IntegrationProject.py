#Corey Record
#Description: This program will be a calorie tracker that will help you either lose or gain weight based on your goals.

def main():

    #Input initial variables
    print("Welcome to the app that will help you meet your caloric goal!")
    print()
    weight = float(input("What is your starting weight in pounds? "))
    height = int(input("What is your height in inches? "))
    gender = str(input("What is your gender? male/female "))
    age = int(input("What is your age? "))
    goal = str(input("What is your goal? gain/lose/maintain "))
    print()
    bmr = 0   
   

    #run if statement if gender is male
    if gender == "male":
        #calculate basal metabolic rate based on goal
        if goal == "lose":
            bmr = ((10 * weight) + (6.25 * height) - (5 * age)) - 200
        if goal == "maintain":
            bmr = ((10 * weight) + (6.25 * height) - (5 * age))
        if goal == "gain":
            bmr = ((10 * weight) + (6.25 * height) - (5 * age)) + 200

        #run if statement if gender is female
    if gender == "female":
        #calculate basal metabolic rate based on goal
        if goal == "lose":
            bmr = ((10 * weight) + (6.25 * height) - (5 * age) -161) - 200
        if goal == "maintain":
            bmr = ((10 * weight) + (6.25 * height) - (5 * age) -161)
        if goal == "gain":
            bmr = ((10 * weight) + (6.25 * height) - (5 * age) -161) + 200
            
    print("Daily calorie goal is ", format(bmr, ".0f"), " calories", sep="")
    print()

    #defines how many meals 
    meal_count = int(input("How many meals did you eat today? "))
    total = 0

    #takes the amount of meals and adds the calories
    for x in range(meal_count):
        meal_cal = int(input("How many calories were in one of your meals? "))
        total += meal_cal
    #calculate basal metabolic rate based on goal
    if total >= (bmr - 100) and total <= (bmr + 100):
        print("You have eaten in the calorie goal")
    if total < (bmr - 100):
        print("You have eaten in a calorie defecit")
    if total > (bmr + 100):
        print("You have eaten in a calorie surplus")

    print()
    
    #defines if cardio is performed
    cardio = str(input("Did you perform cardio? yes/no "))
    caloriesBurned = 0
    #run if cardio is yes
    if cardio == "yes":
        #calculates the calories burned based on type of cardio and how much 
        cardiotype = str(input("What type of cardio? run/walk/cycle "))
        if cardiotype == "run":
            miles = float(input("How many miles did you run? "))
            caloriesBurned = miles * 170  
        elif cardiotype == "walk":
            miles = float(input("How many miles did you walk? "))
            calroiesBurned = miles * 100 
        elif cardiotype == "cycle":
            miles = float(input("How many miles did you cycle? "))
            caloriesBurned = miles * 60
        print("You have burned ", format(caloriesBurned, ".0f"), " calories.", sep="")

        print()
        
    #run if cardio is no 
    if cardio == "no":
        print("Consider doing cardio to help with your caloric goals.")

    #determines gender for calculation of ideal bodweight and calls the function based on that 
    if gender == "male":
        ibwm = idealBodyweightMen(height)
        print("The ideal bodyweight for your height is: ", ibwm)
    
    else:
        ibwf = idealBodyweightFemale(height)
        print("The ideal bodyweight for your height is: ", ibwf)

#calculates the ideal bodyweight for males at a certain height    
def idealBodyweightMen(height):
    cmHeight = height * 30.48
    return 50 +(0.91 *(cmHeight - 152.4))

#calculates the ideal bodyweight for females at a certain height
def idealBodyweightFemale(height):
    cmHeight = height * 30.48
    return 45.5 +(0.91 *(cmHeight - 152.4))
        
main()

