from questions import questions2, questions_new2

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

for question in questions2:
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
  for question in questions_new2:
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
    index = movie_genres.index("Horror, Sci-Fi")
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