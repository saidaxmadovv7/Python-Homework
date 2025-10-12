from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

# Math operations
print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))
print("Multiply:", multiply(10, 5))
print("Divide:", divide(10, 5))

# String utils
print("Reverse:", reverse_string("Python"))
print("Vowels:", count_vowels("Python Programming"))

# Geometry
print("Area:", calculate_area(7))
print("Circumference:", calculate_circumference(7))

# File operations
write_file("example.txt", "Hello from Python modules!")
print("File content:", read_file("example.txt"))
