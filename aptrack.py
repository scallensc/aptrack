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

#def write_to_file(placeholder, track_num):
#    with open(filename, "w+") as file:
#        file.write(placeholder)

#function for user to input a new tracking number
#saves time having to relaunch program passing argument
#if left out
def in_track(track_num):
    ''' input tracking number '''
    track_num = input(f'\nPlease enter your tracking number: ')
    track_num = track_num.upper()
    if track_num is not '' and not None:
        return track_num
    else:
        print(f'\nNo tracking number entered!')
        track_num = in_track(track_num)
        return track_num

#function to display tracking information
def show_tracking(track_response):
    ''' show tracking number '''
    global track_num

    #Actual API would use https://digitalapi.auspost.com.au/shipping/v1/track?tracking_ids=

    url = 'https://17f59561-efde-4215-b082-f40188ed2ad5.mock.pstmn.io/shipping/v1/track?tracking_ids='

    #follwing code commented out as mock server does not use,
    #actual API would require headers to be sent as follows:
    #headers = ({'Content-Type: application/json',
    #            'Accept: application/json',
    #            'Account-Number: 0000123456',
    #            'Authorization: Basic NjAxYTQwMzItNmRiZC00NmFhLTljNmMtOGM2ZGFjY2E1ZTYxOnBhc3N3b3JkCg==}'})

    query = requests.get(url + track_num) #actual API would require requests.get(url + track_num, headers)
    if query.status_code == 200:
        track_response = query
        if track_num in track_response.text:
            track_response = query.json()
            print(f'\n{track_response}')
            return track_response
        else:
            print(f'\nTracking number not found!')
            return track_num
    else:
        track_response = 'Error!'
        print(f'\n{track_response}')
        return track_response

def menu():
    ''' show menu '''
    global track_num
    track_num = None
    global track_response
    track_response = None
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tracknum', help='run: "aptrack TRACKINGNUMBERHERE to insert tracking number"')
    #parser.add_argument('-h', '--history', help='enable history stored as TRACKINGNUMBER.txt', action='store_true')
    args = parser.parse_args()
    if args.tracknum is not None:
        track_num = (args.tracknum)
        show_tracking(track_response)
    else:
        print(f'\nIn future, you can also run: aptrack TRACKINGNUMBERHERE to receive most recent tracking status at command line')
        track_num = None
        while True:
            print(f"""
        Active tracking number:

        {track_num}

            1. Enter new tracking number
            2. Show tracking information
            3. Show History
            4. Exit
            """)
            menu_choice = input("What would you like to do? (choose 1-4) ")
            if menu_choice == "1":
                track_num = in_track(track_num)
            elif menu_choice == "2":
                if track_num is not '' and track_num is not None:
                    show_tracking(track_response)
                else:
                    print(f'\nNo tracking number present!')
                    track_num = in_track(track_num)
            elif menu_choice == "3":
                track_num = 'History'
                print("\nHistory")
            elif menu_choice == "4":
                print("\nGoodbye")
                break
            else:
                print("\nInvalid choice, please try again")

menu()
