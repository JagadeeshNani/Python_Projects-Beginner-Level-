""" 
Mad Libs Generator
--------------------

Mad Libs Generator teaches to manipulate user-Inputted
data as the Mad Libs refer to a series of inputs that a user
enters.The input from the user could be anything from an 
adjective, a pronoun, or even a verb. After all the inputs are 
entered the application takes all the data and arranges it build
to a story template.
"""

# Loop back to this point once code finishes

loop = ""
while (loop != "no"):
# All the questions that the program asks the user
	noun = input("Choose a noun: ")	
	p_noun = input("Choose a Plural noun: ")
	noun2 = input("Choose a noun: ")
	place = input("Name a place: ")
	adjective = input("Choose an adjective (Describing word): ")
	noun3 = input("Choose a noun: ")
# Displays the story based on the users input
	print("-------------------------------------")
	print("Be kind to your",noun,"- footed", p_noun)
	print("For a duck may be somebody's", noun2,",")
	print("Be kind to your", p_noun,"in",place)
	print("Where the weather is always",adjective,",")
	print()
	print("You may think that is this the",noun3,",")
	print("Well it is.")
	print("----------------------------------------")
# Loop back
	loop = input("Do you want to continue: ").lower()
