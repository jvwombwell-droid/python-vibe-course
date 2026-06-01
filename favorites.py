"""Ask for three favorite things and print them back."""

favorites = {
    "coffee": input("What's your favorite coffee? "),
    "song": input("What's your favorite song? "),
    "city": input("What's your favorite city? "),
}

print("\nYour favorites:")
for category, choice in favorites.items():
    print(f"  {category.title()}: {choice}")
