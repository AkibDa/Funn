from questions import questions1

name = input("Enter your name: ")

print("Welcome to 'Which Princess Are You ?'")

c = 0
r = 0
b = 0
a = 0
e = 0
s = 0
j = 0

for question in questions1:
  print(question[0])

  print(question[1])
  print(question[2])
  print(question[3])
  print(question[4])
  print(question[5])
  print(question[6])
  print(question[7])

  ans = input("Choose your option: ").upper()

  if( ans == 'A'):
    c = c + 1
  elif( ans == 'B'):
    r = r + 1
  elif( ans == 'C'):
    b = b + 1
  elif( ans == 'D'):
    a = a + 1
  elif( ans == 'E'):
    e = e + 1
  elif( ans == 'F'):
    s = s + 1
  elif( ans == 'G'):
    j = j + 1
  else:
    print("Choose between A to G")

if(c>r and c>b and c>a and c>e and c>s and c>j):
  print(f"{name} is Cinderella: Focuses on hope, kindness, and resilience.")
elif(r>c and r>b and r>a and r>e and r>s and r>j):
  print(f"{name} is Rapunzel: Creative, adventurous, and curious.")
elif(b>c and b>r and b>a and b>e and b>s and b>j):
  print(f"{name} is Belle: Intellectual and values inner beauty.")
elif(a>c and a>r and a>b and a>e and a>s and a>j):
  print(f"{name} is Aurora: Dreamy, graceful, and calm.")
elif(e>c and e>r and e>b and e>a and e>s and e>j):
  print(f"{name} is Elsa: Self-reflective, independent, and emotional.")
elif(s>c and s>r and s>b and s>a and s>e and s>j):
  print(f"{name} is Snow White: Cheerful, nurturing, and optimistic.")
else:
  print(f"{name} is Jasmine: Bold, independent, and justice-seeking.")