def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name' : 'Ishika Thakur',
        'student_id': 10325491,
        'pizza_toppings' : ['CHICKEN','CHEESE','PEPPERONI'],
        'movie' : [
            {'title':'sanam teri kasam','genre':'romantic'},
            {'title':'labrynthys','genre':'sci-fi'}
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {'title':'the dark knight','genre':'action'}
    about_me['movies'].append(new_movie)

    print_student_name_and_id(about_me)

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me['full_name']
    first_name = full_name.split()[0]
    student_id = about_me['student_id']
    print(
        f'My name is {full_name}, but you can call me Ms. {first_name}.\nMy student ID is {student_id}.'
    )
    return
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    about_me['pizza_toppings'] = sorted(about_me['pizza_toppings'])
    about_me['ppizza_toppings'] = [topping.lower() for topping in about_me['pizza_toppings']]
    return
# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for topping in about_me['pizza_toppings']:
        print(f"- {topping.capatalize()}")
    print()
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie['genre'] for movie in about_me['movies']]
    print(f"I like to watch {', '.join(genres)} movies.\n")
    return


# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie['title'] for movie in movie_list]
    print(f"Some of my favourite movies are {', '.join(titles)}!\n")
    return
    
if __name__ == '__main__':
    main()