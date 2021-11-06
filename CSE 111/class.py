def get_username():
    username = input('Please enter your name: ')
    return username

def get_favorite_movies(username):
    favorite_movies = []
    while(True):
        movie_string = input(f'{username}, please enter your favorite movie: ')
        
        if(movie_string == 'N'):
            break
        get_favorite_movies(name)
    return favorite_movies
            

name = get_username()

movies = get_favorite_movies(name)

for m in movies:
    print

#writing functions
def count_to_number(number, skip):
    for i in range(10, number, skip):
        print(i)

def main():
    max = int(input('how high do you want to count: '))
    step = int(input('enter how you want to count: ' ))
    count_to_number(max, step)

main()



