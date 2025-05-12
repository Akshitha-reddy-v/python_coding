# printing Hello World! on the console - single line comment
print("Hello World!")
""" Taking a string from user as input
    giving reversed and uppercase string as output to console
    - multi line comments
"""
def reverse_str(s):
  return s[::-1]
str = input("Enter a string : ")
reversed_str = reverse_str(str)
print(reversed_str.upper())
