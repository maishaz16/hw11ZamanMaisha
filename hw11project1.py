# Exercise No.   1
# File Name:     hw11project1.py
# Programmer:    Maisha Zaman
# Date:          July 25, 2020
#
# Problem Statement: Create a program that counts the reserved words in a python file.
#
# Overall Plan:
# 1. Print Code Introduction
# 2. Ask user to input file name to be read
# 3. read file as one long string
# 4. split the words into a file
# 5. Count the number of words in list
# 6. Print results to user


def hw11project11():

    ## Print Code introduction
    print("This program counts the reserved words in a file")

    ## Ask user to input file name to be red
    fname = input("File to analyze (i.e reservedwords.txt): ")

    # read file as one long string
    text = open(fname, "r").read()

    # split the words into a file
    words = text.split()

    # Count the number of words in list
    num = len(words)

    # Print results to user
    print("The number of words in {0} is {1}".format(fname,num))


hw11project11()
