raining = input("Is it raining? (yes/no) ").strip().lower()
umbrella = input("Do you have an umbrella? (yes/no) ").strip().lower()

if raining == "yes" and umbrella == "no":
    print("Take the umbrella!")
else:
    print("You're good to go!")
