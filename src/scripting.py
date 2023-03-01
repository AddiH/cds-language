# import argparse
# 
# #initialise parser
# parser = argparse.ArgumentParser()
# # add arguments
# parser.add_argument("--name", type=str)
# # parse the arguments from command line
# args = parser.parse_args()
# 
# print(args)
# print(args.name)
# 
# def hello(name):
#     print(f"howdy babe! you look like a {name}")
#     print("what are you doing here " + name + ". It's past your bedtime!")
# 
# hello(args.name)

import argparse # when you import, it runs everything in the files (thats how the functions gets defined)
# so when you write functions you can add if __name__ == "__main__": (see bottom) then what is after that is 
# only run if it is run for command line, not when it is imported as a module

def input_parse():
    #initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--name", type = str, default = "world")
    parser.add_argument("--age", type = int, required=True) # do not even THINK about running the code if age is not defined
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args


def hello(name, age):
    print("what are you doing here " + name + f"!?. It's past your bedtime! You are only {age} years old!")
    print("str() is also good when you're " + str(age) + " years old")

def main():
    # run input parse to get name
    args = input_parse()
    # pass name to hello
    hello(args.name, args.age)

# if this code is called from command line, run main
if __name__ == "__main__": # which file is being read? The __name__ is name of current file, the __main__ is the file being run
    main()