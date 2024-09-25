# Task: Print movie rating meanings
# Objective
#

# Practice using one if statement that uses else if and else
#
# The task
# The if statement you make will below will print the meaning of the movie rating specified at the beginning of the code.
#
# possible film ratings are "universal", "pg", "12", "12a", "15", "18"

film_rating = "12a"

# use an if statement to check for "universal" rating

if film_rating == "universal":
    print("all age groups can watch this film")

elif film_rating == "pg":
    print("General viewing, but some scenes may be unsuitable for young children.")

elif film_rating in ["12","12a"]:
    print(
     "Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")

elif film_rating == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")

elif film_rating == "18":
    print("No one younger than 18 may see an 18 film in a cinema.")

else:
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")

