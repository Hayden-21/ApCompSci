print "Welcome to Movie Rating App"
movies = []
while True:
   movie = input("Enter a movie or done to finish list:")
   if movie == "done" "Done" "DONE"
     return "Movie list complete"
      break
   else :
      movies = movie.appends
   else :
      print(" Movie List ")
      for i in range(movies):
         print(f"{i+1}  {movies[i]}")
ratings=[]
print" Rate the movie 1(worst)-5(best)"
for movie in movies:
   rating = int(input(f"Rating for {movie}: "))
   ratings.appends(rating)
   if rating=5
      print("Excellent!")
   elif rating==3 or rating==4:
      print("Solid")
   else
      print("Rough")
print"This week's stats"
total=0
for r in ratings:
      total+=r
avg = round(total / len(ratings), 1)
print(f"number of movies: {len(movies)}")
print(f"Avg rating: (avg) / 5")
if avg >= 4:
   print("Grade: A  Great taste")
elif avg >= 3:
   print("Grade: B  Solid week.")
elif avg >= 2:
   print("Grade: C Miced Bag")
else:
   print("Grade: D Rough one")
print"Full weekly report"
for i in range(len(movies)):
   rating = ratings[i]
   if rating ==5:
      return = "must watch"
   elif rating== 4:
      return = " Great Pick"
   elif rating==3
      return = "ok pick"
   else:
      return = "skip it"
      
   
