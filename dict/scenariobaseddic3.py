#  Create a dictionary to store movie ratings:
# pythonmovies = {"Inception": 9.0, "Interstellar": 8.6, "Tenet": 7.5}
# Write a program to:
# Add a new movie "Dunkirk" with rating 8.0
# Find movie with highest rating
# List all movies with rating above 8.0
Movies_series={'From':9.9,'Home_alone':9.1,'Fall':8.5,'Interstellar':9.0,'All of us are dead':9.95}
Movies_series['Dunkirk']=8.0
Highest_Rating=0
for key,value in Movies_series.items():
    if value>Highest_Rating:
        Highest_Rating=value
        movie=key

    if value>9:
        print(key)
print(movie)


    
