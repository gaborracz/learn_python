score = input("Please enter a score (floating point number) between 0.0 and 1.0: ")

try:
    score_float = float(score)
except:
    print("You've entered invalid data, please try again and enter a floating point number between 0.0 and 1.0")
    quit()

if score_float > 1.0 :
    print("The entered number cannot be more than 1.0 \nPlease try again and choose a number from the valid range 0.0 - 1.0")
    quit()
elif score_float < 0.0 :
    print("The entered number cannot be negative. \nPlease try again and choose a number from the valid range 0.0 - 1.0")
    quit()
else:
    if score_float >= 0.9 :
        print("A")
    elif score_float >= 0.8 :
        print("B")
    elif score_float >= 0.7 :
        print("C")
    elif score_float >= 0.6 :
        print("D")
    else :
        print("F")