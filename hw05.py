"""
Name: Ash Rulifson
Peers: office hours with Jordan
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
            if up_let == "A" or up_let == "B" or up_let == "C":
                return up_let
            else:
                print("Error: You provided the wrong character.")
                up_let = input("Give a single uppercase letter: ")
        else: # initial request for input
            up_let = input("Give a single uppercase letter: ")
    # if very first input was perfect:
    return up_let

def get_digit():
    """ pester user for a 1, 2 or 3 until they do it """
    num_key = "0"
    num_key = input("Give a single number character: ")
# ask if it is an invalid input. if it is:
    while num_key != "1" and num_key != "2" and num_key != "3":
        # check if they provided a digit. no digit:
        if not num_key.isdigit():
            print("Error: your input should be only digits.")
            num_key = input("Give a single number character: ")
            continue
        # they did provide a digit:  check if it's between 1 and 3
        elif num_key == "1" or num_key == "2" or num_key == "3": # right range
            break
        else: # it's not between 1 and 3
                print("Error: a single digit needs to be in [1,3].")
                num_key = input("Give a single number character: ")
                continue
# if the input was valid:
    return num_key
    


def check_pattern(letter, digit, lst):
    """ check the list for strings that contain provided letter and digit in same order """
    
    for item in lst:
        if letter in item:
            str_len = len(item)
            count = 0
            if digit not in item: # can't be this one, move on
                continue
            else: # if both digit and letter are in the list item, check order
                first = ""
                for char in item[0:str_len]:
                    count += 1
                    if char == letter or char == digit:
                        # 'first' and 'second' are variables 
                        while first == "" and char != digit:
                            # first has not been filled already and will now be filled
                            # by a letter
                            first = item[count-1]
                            break
                        while first != "" and char == digit:
                            # first has been filled and second will now be filled by
                            # a digit
                            second = item[count-1]
                            while item not in match:
                                # add the item that matches letter and number in the
                                # right order (letter first, digit second) to a list of
                                # only strings that match, but only if the matching
                                # string has not already been added (so ex. C2C2 only
                                # gets printed once)
                                match.append(item)
                            break
                    
                else:
                    continue          
            
        else: # can't be this list item, move to the next one in the list
            continue
        
        
    # print out all matching values in the right format
    print("Strings with the pattern:")
    for elem in match:
        print(elem, end = " ")
    print()


def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    global st_list
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]
    

    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    again = "y"
    while again == "y":
        global match
        match = list()
        letter = get_letter()
        digit = get_digit()
        check_pattern(letter, digit, st_list)
        again = input("Try Again? (y/n): ")

    # -------------------------------------------------
    # No need to modify anything below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()
