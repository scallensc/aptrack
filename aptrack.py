#!/usr/bin/python
"""
Author: Samuel C Allen
Contact: samuelcallen@me.com
Date: 2019/06/29
Licence: GPLv3
Version: 0.1
"""
import argparse
import requests

#def write_to_file(placeholder, tracking_number):
#    with open(filename, "w+") as file:
#        file.write(placeholder)

#Australia Post RESTFUL auth requirement example headers:
#https://digitalapi.auspost.com.au/shipping/v1/track?tracking_ids=
#Content-Type: application/json
#Accept: application/json
#Account-Number: 0000123456
#Authorization: Basic NjAxYTQwMzItNmRiZC00NmFhLTljNmMtOGM2ZGFjY2E1ZTYxOnBhc3N3b3JkCg==

#URL = 'https://digitalapi.auspost.com.au/shipping/v1/track?tracking_ids='
#url = 'http://localhost:3000/tracking_results' #DUMMY URL Local JSON server
#headers = ({'Content-Type: application/json',
#            'Accept: application/json',
#            'Account-Number: 0000123456',
#            'Authorization: Basic NjAxYTQwMzItNmRiZC00NmFhLTljNmMtOGM2ZGFjY2E1ZTYxOnBhc3N3b3JkCg==}'})

#function for user to input a new tracking number
#saves time having to relaunch program passing argument
def new_tracking_number(tracking_number):
    ''' input tracking number '''
    input_tracking_number = input(f'Please enter your tracking number: ')
    input_tracking_number = input_tracking_number.upper()
    return input_tracking_number

#function to display tracking information
def show_tracking(response):
    ''' show tracking number '''
    url = 'http://localhost:3000/tracking_results' #DUMMY URL Local JSON server
    headers = ({'Content-Type: application/json',
                'Accept: application/json',
                'Account-Number: 0000123456',
                'Authorization: Basic NjAxYTQwMzItNmRiZC00NmFhLTljNmMtOGM2ZGFjY2E1ZTYxOnBhc3N3b3JkCg==}'})
    query = requests.get(url)
    response = query.json()
    print(response)

def menu():
    ''' show menu '''
    response = None
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tracknum', help='run: "aptrack TRACKINGNUMBERHERE to insert tracking number"')
    #parser.add_argument('-h', '--history', help='enable history stored as TRACKINGNUMBER.txt', action='store_true')
    args = parser.parse_args()
    if args.tracknum is not None:
        tracking_number = (args.tracknum)
        show_tracking(response)
    else:
        print(f'\nIn future, you can also run: aptrack TRACKINGNUMBERHERE to receive most recent tracking status at command line')
        tracking_number = None
        while True:
            print(f"""
        Active tracking number:

        {tracking_number}

            1. Enter new tracking number
            2. Show tracking information
            3. Show History
            4. Exit
            """)
            ans = input("What would you like to do? (choose 1-4) ")
            if ans == "1":
                tracking_number = new_tracking_number(tracking_number)
            elif ans == "2":
                show_tracking(response)
                #break
            elif ans == "3":
                tracking_number = 'History'
                print("\nHistory")
            elif ans == "4":
                print("\nGoodbye")
                break
            else:
                print("\nInvalid choice, please try again")

menu()
