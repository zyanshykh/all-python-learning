# --- OPERATORS, TYPE CASTING & CONDITIONS ---

# 1. Type Casting (Input humesha text hota hai, use number banana)
birth_year = input("What year were you born? (e.g., 2000): ") # Input as string
# Text ko integer (number) me convert karna padega taake math kar sakein
birth_year = int (birth_year)

current_year = 2026
calculated_age = current_year - birth_year

print(f"Calculated Age: You are {calculated_age} years old.\n")

# 2. If-Else Conditions (Smart Decision Making)
if calculated_age >=18:
    print("🚀 Status: You can work on professional AI projects!")
else:
    print("📈 Status: You are still learning, keep growing!")