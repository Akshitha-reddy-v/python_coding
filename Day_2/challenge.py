""" Challenge - To swap first and last characters
    from the string input prompted by the user 
    if length of string is 1, return same string """
def swap_first_last_char(s):
  if len(s) < 2 :
    return s
  return s[-1] + s[1:-1] + s[0]

text = input("Enter the string : ")
swapped_text = swap_first_last_char(text)
print(swapped_text)
