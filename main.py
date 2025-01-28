name = input("Enter your name: ")

print("Welcome to 'Which Princess Are You ?'")

c = 0
r = 0
b = 0
a = 0
e = 0
s = 0
j = 0

questions = [['How do you handle challenges?','A) Stay hopeful and endure with grace.','B) Face them head-on with courage and curiosity.','C) Think critically and look for solutions.','D) Take control and work on self-improvement.','E) Maintain cheerfulness and lean on your support system.','F) Stay calm and let things unfold naturally.','G) Stand up and fight for what I believe in.'],['What is your ideal way to spend a day?','A) Making the most of what you have and staying optimistic.','B) Exploring nature or a new place.','C) Reading and learning something new.','D) Working on yourself and mastering a skill.','E) Helping others and making their day brighter.','F) Relaxing and dreaming about the future.','G) Standing up for a cause or seeking adventure.'],['What is most important to you in life?','A) Love and kindness','B)Adventure and discovery.','C) Knowledge and growth.','D) Inner peace and self-acceptance.','E) Spreading happiness and joy.','F) Harmony and beauty.','G) Freedom and independence'],['What kind of people do you surround yourself with?','A) Hardworking and humble individuals','B) Brave, adventurous individuals.','C) Those who appreciate my uniqueness.','D) Those who bring calm and peace to my life.','E) People who understand my complexity.','F) Kind and supportive people.','G) People who respect my independence '],['What is your dream destination?','A) Anywhere as long as I am surrounded by love.','B) A towering castle overlooking a kingdom.','C) A library full of books.','D) A peaceful castle or meadow.','E) A magical ice palace.','F) A cozy cottage in the woods.','G) A lively and vibrant marketplace']]

for question in questions:
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

if(c>r or c>b or c>a or c>e or c>s or c>j):
  print(f"{name} is Cinderella: Focuses on hope, kindness, and resilience.")
elif(r>c or r>b or r>a or r>e or r>s or r>j):
  print(f"{name} is Rapunzel: Creative, adventurous, and curious.")
elif(b>c or b>r or b>a or b>e or b>s or b>j):
  print(f"{name} is Belle: Intellectual and values inner beauty.")
elif(a>c or a>r or a>b or a>e or a>s or a>j):
  print(f"{name} is Aurora: Dreamy, graceful, and calm.")
elif(e>c or e>r or e>b or e>a or e>s or e>j):
  print(f"{name} is Elsa: Self-reflective, independent, and emotional.")
elif(s>c or s>r or s>b or s>a or s>e or s>j):
  print(f"{name} is Snow White: Cheerful, nurturing, and optimistic.")
else:
  print(f"{name} is Jasmine: Bold, independent, and justice-seeking.")