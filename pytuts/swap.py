# Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the original numbers
print("\nOriginal Numbers:")
print(f"First Number: {num1}")
print(f"Second Number: {num2}")

# Swap the numbers
temp = num1
num1 = num2
num2 = temp

# Display the swapped numbers
print("\nSwapped Numbers:")
print("First Number: {num1}")
print(f"Second Number: {num2}")
