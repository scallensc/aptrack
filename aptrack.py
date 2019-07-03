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
#import json commented out as requests library contains json parser

#def write_to_file(placeholder, track_num):
#    with open(filename, "w+") as file:
#        file.write(placeholder)

#function for user to input a new tracking number
#saves time having to relaunch program passing argument
#if left out
def in_track():
    ''' input tracking number '''
    track_num = input(f'\nPlease enter your tracking number: ')
    track_num = track_num.upper()
    if track_num != '' and track_num is not None:
        return track_num

    print(f'\nNo tracking number entered!')
    track_num = in_track()
    return track_num

#function to display tracking information
def show_tracking(track_num):
    ''' show tracking number '''

    #Actual Australia Post API would use the following as url
    #url = 'https://digitalapi.auspost.com.au/test/shipping/v1/track?tracking_ids=' for testing
    #url = 'https://digitalapi.auspost.com.au/shipping/v1/track?tracking_ids=' for production

    url = 'https://8b7a028c-6934-451c-9619-f683a4367494.mock.pstmn.io/shipping/v1/track?tracking_ids='

    #actual Australia Post API would require headers to be sent as follows:
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Account-Number': '00001234567',
        'Authorization': 'Basic YWJjZDEyMzQtZmRlNy00ODczLWE1NDYtNzY1ZmEyZmU3NDE2OlBhc3N3b3Jk'
    }

    if track_num is not None:
        query = requests.get(url + track_num)#, headers) #actual API would require requests.get(url + track_num, headers)

        if query.status_code == 200:
            track_response = query

            if track_num in track_response.text:
                track_response = query.json()
                #print(f'\n{track_response}')
                for result in track_response['tracking_results']:
                    print(f'\n' + result['status'])
                #for tracking_id in track_response.items():
                #    print(track_response[status])
                error_response = None
                return error_response

        else:
            error_response = query
            return error_response

def show_menu():
    ''' show menu '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tracknum', help='run: "aptrack TRACKINGNUMBERHERE to receive most recent tracking info at command line"')
    #parser.add_argument('-h', '--history', help='enable history stored as TRACKINGNUMBER.txt', action='store_true')
    args = parser.parse_args()

    if args.tracknum is not None:
        track_num = (args.tracknum)
        show_tracking(track_num)
        quit()

    print(f'\nIn future, you can also run: aptrack -t TRACKINGNUMBERHERE to receive most recent tracking status at command line')

    track_num = None
    error_response = None

    while True:
        print(f"""
    Active tracking number: {track_num}
    Current errors:  {error_response}

        1. Enter new tracking number
        2. Show current tracking information
        3. Show tracking history
        4. Exit
        """)
        menu_choice = input("What would you like to do? (choose 1-4) ")

        if menu_choice == "1":
            track_num = in_track()
            error_response = None

        elif menu_choice == "2":
            if track_num != '' and track_num is not None:
                error_response = show_tracking(track_num)

            else:
                print(f'\nNo tracking number present!')
                track_num = in_track()
                error_response = show_tracking(track_num)

        elif menu_choice == "3":
            print("\nHistory")

        elif menu_choice == "4":
            print("\nGoodbye")
            break

        else:
            print("\nInvalid choice, please try again!")

show_menu()
