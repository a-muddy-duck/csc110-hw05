"""
Name: Ash Rulifson
Peers: (add any collaborators)
References: (anything you checked to solve this)
Due: October 23, 2026
"""

def get_letter():
    """ ask user for a single letter, A, B, or C, until they provide a valid input. """
    up_let = ":-)"
    while (len(up_let) != 1) or (up_let != ("A" or "B" or "C")):
        if up_let != ":-)": # prevents printing error before asking for input
            if len(up_let) != 1:
                print("Error: it needs to be a single character.")
                up_let = input("Give a single uppercase letter: ")
            if up_let != ("A" or "B" or "C"):
                print("Error: You provided the wrong character.")
                up_let = input("Give a single uppercase letter: ")
        else: # initial request for input
            up_let = input("Give a single uppercase letter: ")
    return up_let

def get_digit():
    """ Add your own Docstring """
    num_key = "0"
    num_key = input("Give a single number character: ")
# ask if it is more than one digit or outside of [1,3]
    while num_key != "1" and num_key != "2" and num_key != "3":
        # check if they provided a digit. no digit:
        if not num_key.isdigit():
            print("Error: your input should be only digits.")
            num_key = input("Give a single number character: ")
            continue
        else: # they did provide a digit
            # check if it's between 1 and 3
            if num_key == "1" or num_key == "2" or num_key == "3": # works
                break
            else: # it's not between 1 and 3
                print("Error: a single digit needs to be in [1,3].")
                num_key = input("Give a single number character: ")
                continue
    return num_key
    


def check_pattern(letter, digit, lst):
    """ Add your own Docstring """
    # remove the default pass and add your code
    pass


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    #get_letter()
    get_digit()

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()