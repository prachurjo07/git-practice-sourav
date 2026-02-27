
from datetime import date
from utils import add, subtract, multiply

print("Name: Sourav Chakraborty")
print("Today's date:", date.today())

try:
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))

    # Example error test:
    print("Add with error:", add("10", 5))
except ValueError as e:
    print("Error:", e)