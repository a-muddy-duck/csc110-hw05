"""
Name: Ash Rulifson
Peers: (add any collaborators)
References: (anything you checked to solve this)
Due: October 23, 2026
"""

def get_letter():
    """ ask user for a single letter: A, B, or C. Ask until they provide a valid input """
    up_let = ":-)"
    while (len(up_let) != 1) or (up_let != ("A" or "B" or "C")):
        if up_let != ":-)": # prevents printing error before asking for input
            if len(up_let) != 1:
                print("Error: it needs to be a single character.")
                up_let = input("Give a single uppercase letter 14: ")
            if up_let != ("A" or "B" or "C"):
                print("Error: You provided the wrong character.")
                up_let = input("Give a single uppercase letter 17: ")
        else: # initial request for input
            up_let = input("Give a single uppercase letter 19: ")
    return up_let

def get_digit():
    """ Add your own Docstring """
    # remove the default return and add your code
    return 0


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

    get_letter()

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()