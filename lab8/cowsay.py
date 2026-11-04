import sys
from heifer_generator import *


def list_cows(cows):  # Lists the names of all available cows.
    cow_names = []
    for cow in cows:
        cow_names.append(cow.get_name())

    print("Cows available:", " ".join(cow_names))


def find_cow(name, cows):  # Finds a cow object with the desired name.
    for i in range(len(cows)):
        if cows[i].get_name() == name:
            return cows[i]
    return None


def main(args):  # main class of the program.
    cows = HeiferGenerator  # This wouldn't work in zybooks without this.
    cow_list = cows.get_cows()
    if args[1] == "-l":  # Prints list of cows.
        list_cows(cow_list)
        print()
    if args[1] == "-n":  # Prints the message with a certain cow image.
        cow = find_cow(args[2], cow_list)
        if cow is not None:  # Making sure the cow exists.
            print()
            for i in range(len(args)):
                if i >= 3:
                    print(args[i], end=' ')
            print()
            print(cow.get_image())  # Printing the cows picture.
            if isinstance(cow, Dragon):  # Checking if the cow can breathe fire.
                if cow.can_breath_fire():
                    print("This dragon can breathe fire.\n")
                else:
                    print("This dragon cannot breathe fire.\n")
        else:  # If it doesn't exist then it prints the error.
            print(f"Could not find {args[2]} cow!\n")

    elif args[1][0] != "-":  # Prints message with default cow.
        print()
        for i in range(len(args)):
            if i >= 1:
                print(args[i], end=' ')
        print()
        print(cow_list[0].get_image())


if __name__ == "__main__":
    main(sys.argv)
