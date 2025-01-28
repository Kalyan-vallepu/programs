def gcd(a, b):
  """
  This function finds the greatest common divisor of two numbers using Euclid's algorithm.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The greatest common divisor of a and b.
  """
  while b:
    a, b = b, a % b
  return a

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find and print the GCD
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is", result)