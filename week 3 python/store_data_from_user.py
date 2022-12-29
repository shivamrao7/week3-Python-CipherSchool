user = {}
name = input('What is your name')
age = input("what is your age").split(",")
fav_movies = input('your fav movies seprated by ,').split(",")
fav_songs = input("your fav songs")

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs
# print(user)

# loop in dict
for key,value in user.items():
    print(f" {key} :{value}")