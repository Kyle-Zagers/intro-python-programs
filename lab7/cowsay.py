import sys
from heifer_generator import *


def list_cows(cows):
    cow_names = []
    for cow in cows:
        cow_names.append(cow.get_name())

    print("Cows available:", " ".join(cow_names))


def find_cow(name, cows):
    for i in range(len(cows)):
        if cows[i].get_name() == name:
            return cows[i]
    return None


def main(args):
    cow_list = HeiferGenerator().get_cows()
    if args[1] == "-l":
        list_cows(cow_list)
        print()
    if args[1] == "-n":
        if find_cow(args[2], cow_list) is not None:
            print()
        for i in range(len(args)):
            if i >= 3 and find_cow(args[2], cow_list) is not None:
                print(args[i], end=' ')
        if find_cow(args[2], cow_list) is not None:
            print()
        print(find_cow(args[2], cow_list).get_image()
              if find_cow(args[2], cow_list) is not None
              else f"Could not find {args[2]} cow!\n")
    elif args[1][0] != "-":
        print()
        for i in range(len(args)):
            if i >= 1:
                print(args[i], end=' ')
        print()
        print(cow_list[0].get_image())


if __name__ == "__main__":
    main(sys.argv)
