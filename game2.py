print("Welcome to my Movie Reccomendation App")

name = input("Enter your name: ")

ST = 0
AT = 0
DR = 0
TD = 0
FA = 0


movie_names = [
    "Inception", "The Dark Knight", "Interstellar", "The Shawshank Redemption",
    "The Godfather", "Forrest Gump", "The Matrix", "Titanic", "Gladiator",
    "Parasite", "Joker", "The Avengers", "Avatar", "Pulp Fiction",
    "The Lord of the Rings: The Fellowship of the Ring", "Spider-Man: No Way Home",
    "The Silence of the Lambs", "A Quiet Place", "Coco", "John Wick"
]

movie_genres = [
    "Sci-Fi, Thriller", "Action, Crime", "Sci-Fi, Drama", "Drama",
    "Crime, Drama", "Drama, Romance", "Sci-Fi, Action", "Romance, Drama", "Action, Drama",
    "Thriller, Drama", "Drama, Crime", "Action, Sci-Fi", "Sci-Fi, Adventure", "Crime, Drama",
    "Fantasy, Adventure", "Action, Superhero", "Thriller, Horror", "Horror, Sci-Fi",
    "Animation, Family", "Action, Thriller"
]

# for i in range(len(movie_genres)):
#   print(f"{movie_names[i]} - {movie_genres[i]}")

questions = [
    "1. What kind of movie do you enjoy the most?\n"
    "   a) Mind-bending and thought-provoking\n"
    "   b) Action-packed and thrilling\n"
    "   c) Emotional and heartwarming\n"
    "   d) Dark and mysterious\n"
    "   e) Fantastical and adventurous\n",

    "2. Which setting excites you the most in a movie?\n"
    "   a) Outer space or futuristic worlds\n"
    "   b) Urban crime-ridden cities\n"
    "   c) Historical or real-life events\n"
    "   d) Psychological mind games\n"
    "   e) Magical and mythical lands\n",

    "3. How do you like your movie endings?\n"
    "   a) Open to interpretation\n"
    "   b) A satisfying revenge or victory\n"
    "   c) Emotional and touching\n"
    "   d) Twisted and unexpected\n"
    "   e) A grand, heroic climax\n",

    "4. Which element is most important in a movie for you?\n"
    "   a) Thought-provoking concepts\n"
    "   b) Intense action sequences\n"
    "   c) Strong character development\n"
    "   d) Suspense and thrill\n"
    "   e) World-building and epic journeys\n",

    "5. Which of these best describes your personality?\n"
    "   a) A deep thinker and problem solver\n"
    "   b) Bold, energetic, and fearless\n"
    "   c) Emotional and compassionate\n"
    "   d) Mysterious and analytical\n"
    "   e) Dreamer with a love for adventure\n"
]

questions_new = [
    "1. Which of these do you enjoy most in a movie?\n"
    "   a) Laugh-out-loud comedy moments\n"
    "   b) Spine-chilling horror and suspense\n"
    "   c) Heartfelt animation with meaningful messages\n"
    "   d) Real-life stories based on true events\n"
    "   e) Fast cars, heists, and high-speed chases\n",

    "2. What kind of protagonist do you prefer?\n"
    "   a) A funny and witty character\n"
    "   b) Someone trying to survive against all odds\n"
    "   c) A lovable hero with a big heart\n"
    "   d) A historical figure or someone from real life\n"
    "   e) A daring risk-taker who lives on the edge\n",

    "3. How do you want a movie to make you feel?\n"
    "   a) Entertained and cheerful\n"
    "   b) On the edge of your seat, scared but excited\n"
    "   c) Nostalgic and emotional\n"
    "   d) Inspired by real-life struggles and achievements\n"
    "   e) Pumped up with adrenaline\n",

    "4. What type of movie setting excites you the most?\n"
    "   a) A hilarious, everyday situation that goes wrong\n"
    "   b) An abandoned house or a haunted place\n"
    "   c) A vibrant and colorful fantasy world\n"
    "   d) A historical war zone or courtroom drama\n"
    "   e) A high-stakes city full of action\n",

    "5. Which famous quote best represents your movie taste?\n"
    "   a) 'Why so serious?'\n"
    "   b) 'Do you like scary movies?'\n"
    "   c) 'Just keep swimming.'\n"
    "   d) 'You can't handle the truth!'\n"
    "   e) 'I live my life a quarter mile at a time.'\n"
]

for question in questions:
  print(question)
  ans = input("Choose any option: ").lower()

  if(ans == 'a'):
    ST = ST + 1
  elif(ans == 'b'):
    AT =AT + 1
  elif(ans == 'c'):
    DR = DR + 1
  elif(ans == 'd'):
    TD = TD + 1
  else:
    FA = FA + 1

if(ST>AT and ST>DR and ST>TD and ST>FA):
  index = movie_genres.index("Sci-Fi, Thriller")
  print(f"We recommend {movie_names[index]} to {name}")
elif(AT>ST and AT>DR and AT>TD and AT>FA):
  index = movie_genres.index("Action, Thriller")
  print(f"We recommend {movie_names[index]} to {name}")
elif(DR>ST and DR>AT and DR>TD and DR>FA):
  index = movie_genres.index("Drama, Romance")
  print(f"We recommend {movie_names[index]} to {name}")
elif(TD>ST and TD>AT and TD>DR and TD>FA):
  index = movie_genres.index("Thriller, Drama")
  print(f"We recommend {movie_names[index]} to {name}")
else:
  index = movie_genres.index("Fantasy, Adventure")
  print(f"We recommend {movie_names[index]} to {name}")



def more():
  D = 0
  H = 0
  AF = 0
  BD = 0
  AC = 0
  for question in questions_new:
    print(question)
    ans = input("Choose any option: ").lower()

    if(ans == 'a'):
      D = D + 1
    elif(ans == 'b'):
      H = H + 1
    elif(ans == 'c'):
      AF = AF + 1
    elif(ans == 'd'):
      BD = BD + 1
    else:
      AC = AC + 1

  if(D>H and D>AF and D>BD and D>AC):
    index = movie_genres.index("Drama")
    print(f"We recommend {movie_names[index]} to {name}")
  elif(H>D and H>AF and H>BD and H>AC):
    index = movie_genres.index("Horror")
    print(f"We recommend {movie_names[index]} to {name}")
  elif(AF>D and AF>H and AF>BD and AF>AC):
    index = movie_genres.index("Animation, Family")
    print(f"We recommend {movie_names[index]} to {name}")
  elif(BD>D and BD>H and BD>AF and BD>AC):
    index = movie_genres.index("Drama, Crime")
    print(f"We recommend {movie_names[index]} to {name}")
  else:
    index = movie_genres.index("Action, Crime")
    print(f"We recommend {movie_names[index]} to {name}")

wer = input("Did u like our reccomendation?\nYes or No: ").lower()
if(wer == 'yes'):
  print("We are happy to help you")
else:
  print("Ok, Answer 5 more questions")
  more()