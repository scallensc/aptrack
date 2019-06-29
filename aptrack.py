#!/usr/bin/python
"""
Author: Samuel C Allen
Contact: samuelcallen@me.com
Date: 2019/06/29
Licence: GPLv3
Version: 0.1
"""
import argparse
import json

#def write_to_file(placeholder, tracking_number):
#    with open(filename, "w+") as file:
#        file.write(placeholder)

#function to display current tracking number
def show_tracking(tracking_number):
    ''' show tracking number '''
    print(tracking_number)

#function for user to input a new tracking number
#saves time having to relaunch program passing argument
def new_tracking_number(tracking_number):
        ''' input tracking number '''
        input_tracking_number=input(f'Please enter your tracking number: ')
        input_tracking_number=input_tracking_number.upper()
        new_tracking_number=input_tracking_number
        return(new_tracking_number)

def menu():
    ''' show menu '''
    parser = argparse.ArgumentParser()
    parser.add_argument('arg_tracking_number', help='run the application with the tracking number after the program name: "aptrack TRACKINGNUMBER"')
    args = parser.parse_args()
    tracking_number = args.arg_tracking_number

    while True:
        print(f"""
        Tracking number: {tracking_number}
        1. Enter new tracking number
        2. Tracking information
        3. History
        4. Exit/Quit
        """)
        ans=input("What would you like to do? ")
        if ans=="1":
            tracking_number = new_tracking_number(tracking_number)
        elif ans=="2":
            print(f"\nDisplaying tracking information for: {tracking_number}")
        elif ans=="3":
            print("\nHistory")
        elif ans=="4":
            print("\nGoodbye")
            break
        else:
            print("\nInvalid choice, please try again")

menu()


