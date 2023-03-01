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

import argparse

def input_parse():
    #initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--name", type=str)
    parser.add_argument("--age", type=str)
    # parse the arguments from command line
    args = parser.parse_args()
    # get the name
    name = args.name
    age = args.age
    return name, age


def hello(name, age):
    print("what are you doing here " + name + ". It's past your bedtime!, you are only " + age + " years old!")

def main():
    # run input parse to get name
    name, age = input_parse()
    # pass name to hello
    hello(name, age)

main()