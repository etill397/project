# Erin Tilling 
# COMP 1701 Fall 2025
# Instructor: Fatemeh Shirzad Phd.
# December 9th 2025

# A program that reads data from a .csv file to a table, takes commands from a user 
# to perform operations on the data including saving the current table to a .csv file.

# Reference

# [1] F. Shirzad. (2025). Advanced topics [PDF slides]. Available: https://learn.mru.ca/d2l/le/content/138191/viewContent/1776515/View

import a3_1701_et_module as module


def main():
    """ Command Line Interface (CLI)"""

    print("Starting...")
    prompt = "Enter command: "
    command = input(prompt)
    command = command.lower()
    current_table = []

    while command != "exit":

        table = module.execute_(command, current_table)
        current_table = table

        command = input(prompt)
        command = command.lower()

    if command == "exit":
        print("Exiting...")

main()