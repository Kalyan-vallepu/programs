def reverse(name):
  reversed_name = ""
  for char in name[::-1]:
    reversed_name += char
  return reversed_name

name = "karthik"
reversed_name = reverse(name)
print(reversed_name) 
