# NameGenderQuery.py

# Query a user for their name and gender. 
# Then, generate a response based off that information.

# @ItsPrestonDavis - Twitter, Github

def askName():
    # Ask the user to input their name.
    name = raw_input("What is your name?")
    # If the name they have entered is blank, alert them and try again.
    if name == "":
        print ("Looks like you didn't enter your name! Let's try that again! \n")
        return askName()
    # Otherwise, return the name they have entered.
    else:
        return name 
    
def askGender():
    # Ask the user to input their gender, either male or female. (M/F)
    gender = raw_input("Are you a male or female? (M/F)").upper()
    # If the user has specified male..
    if gender == "M":
        gender = "male"
        return gender
    # If the user has specified female..
    elif gender == "F":
        gender = "female"
        return gender
    # If the user has not specified their gender..
    elif gender == "":
        # Alert the user and try again.
        print ("Looks like you didn't enter your gender! Let's try that again! \n")
        return askGender()
    # If the user has not entered any input, alert them and try again.
    else:
        print ("Looks like you entered something other than male or female! Let's try that again! \n")
        return askGender()

# Assign strings to the appropriate variables.
name = askName() 
gender = askGender()

# Print some generated output (based on the input the user has provided).
print "Therefore, your name is %s and you are a %s!" % (name, gender)

    
