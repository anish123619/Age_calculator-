# Step 1: Ask the user to enter their birth year
birth_year = int(input("Enter your birth year: "))

# Step 2: Import the current year from datetime
from datetime import datetime
current_year = datetime.now().year

# Step 3: Calculate the age
age = current_year - birth_year

# Step 4: Display the result
print("You are", age, "years old.")