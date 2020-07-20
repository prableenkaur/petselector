# Constants are typically all caps to denote that the value of these variables 
# should not change or be manipulated over the course of the program
# Qualities for each animal
CAT_QUALITIES = ['Affectionate with family', 'Amount of shedding', 'Easy to groom']
DOG_QUALITIES = ['Adaptability', 'All around friendliness', 'Exercise needs']

def main():
    '''Determine which animal the user is looking for. Then ask which qualities they
    would like their animal to have.
    '''
    #Ask the user if they want a dog or cat
    animal = raw_input("Would you like a cat or a dog?\n>> ")

    #Tell the user what animal they selected 
    if animal == "cat":
        print('You selected ' + animal)
    elif animal == "dog":
        print('You selected ' + animal)
    else:
        print("That input was invalid. Try again.")

    # get qualities function

    # Print their qualities

def get_qualities(qualities_list):
    '''Get user raw_input for which qualities they are looking for in an animal.
    
    Parameters:
    qualities_list (list): list of all qualities for an animal type

    Returns:
    list: list of qualities the user is looking for
    '''
    qualities = []
    selection = -1

    # keep track of all the qualities # parameter
    # keep track of qualities already used # list
    while true
    #     get remaining qualities (parameter minus already used) #list
    #     response = raw_input(formatQuestion(remaining qualities))
    #     print response
    #     if they press done OR remaining qualities is empty:
    #         break


    # # Use a while loop to ask the user which qualities they are looking for
    # while selection != (): #<-- #TODO fill in
    #     # Get user raw_input and store it in the selection variable
    #     # Note that we are converting the raw_input string to an integer that can be used for comparison
    # selection = int(raw_input(""))

    #     #If/else block to check for valid choice, "done", or invalid number
    # if (): #valid choice
    #         #Append the quality to qualities variable
    # elif (): #done
    #         #Return the qualities list
    # else: 
    #         #Print that the user choice was invalid
    
def gen_qualities_text(qualities_list):
    '''
    Generate output text containing all qualities to display to the user.

    Parameters:
    qualities_list (list): list of all qualities for an animal type

    Returns:
    str: String with each quality on a separate, numbered line. Includes an additional numbered line for "Done"
    '''
    qualities_string = ''
    #For each index in the qualities list, make a line like "1. <quality>"
    for i in range(len(qualities_list)):
        return fkasjdhfkj
        # Append the number (e.g. "1. ") to the string
        # Append the quality (e.g. "Adaptability") to the string

    # Append the Done line to the string
    # Append the prompt ">> " to the string

    #Return the string

if __name__ == '__main__':
    # You can change the function down here to test other functions
    # E.g. you could put 'print(gen_qualities_text(CAT_QUALITIES))' to see if the output for that
    # function is what you think it should be

    # param - list of numbers
    # output - 10th negative number in the list

    # numbers = [] # argument (list of numbers)

    # keep track of how many negative numbers
    # keep track of the current number
    # while still looking (hit negative number count OR finished looking at the list):
    #     get a new number
    #     check if negative number -> if negative, increase my counter, else continue

    # negative_number_count = 0
    # current_index = 0
    # while negative_number_count < 10 and current_index < len(numbers):
    #     current_number = numbers[current_index]
    #     if current_number < 0:
    #         negative_number_count = negative_number_count + 1
    #     current_index = current_index + 1


    main()
