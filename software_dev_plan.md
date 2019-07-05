# CSB-SYD-19 A2 Terminal Application

### Australia Post delivery status

The purpose of this application is for a user to be able to receive information regarding the status of a delivery from Australia Post, from the terminal, instead of having to utilise the Australia Post website to retrieve such information. Using the Python requests library, It will retrieve the information via an HTTP GET request, utilising the Australia Post track/trace API, which will return information in JSON format, which will then be parsed and output to the user in a human readable form. This information will also be stored in a history file.

Being someone that finds themselves refreshing the Australia Post website constantly while waiting for a delivery, I feel that for a developer working in terminal frequently, it would be quite handy to have the ability to quickly get a status update from the command line instead of utilising the web page to retrieve this information.

The target audience for this application would be anyone awaiting a delivery from Australia Post that would like to receive information on the delivery status via the terminal, developers, or anyone using terminal frequently on a daily basis that receive postal deliveries. Perhaps employees in the mail department of a business or corporation that receive a lot of packages and utilise a terminal based workflow.

The application will be used as a command in terminal, with the option of the package tracking number being passed to the application command as an argument. Using argparse library, the application will determine if the user has or has not passed the tracking number using an optional argument flag. This will then be checked for validity using the Australia Post API, if the user has passed a tracking number to the application, and the number is valid, the most recent tracking update will be delivered to the command line and the program will exit. If invalid, the user will be given a relevant error code and the application will also exit. If the user has not passed a tracking number as an argument, they will have a menu with options to input a valid tracking number, after which they can view tracking information, history, or have a choice to exit the application.

## Development Plan

### Features

#### Two use case scenarios, user passes tracking number with argument, or enters no tracking number on program run

- Tracking number passed as argument - Display most recent tracking event for valid number at command line and break, on error, display relevant error message at command line and break
- Tracking number not passed as argument - Display menu with active tracking number at the top and options

#### _Display menu_

- Inform user of option for future use to pass tracking number as argument to receive most recent tracking update at command line

- Show menu with following options
  - _Enter new tracking number_
    - Allow user to enter a new tracking number
  - _Show tracking information_
    - Check entered number for validity using Australia Post API
    - Valid result will return most recent tracking event information for active tracking number
    - Invalid result will ask user to enter a valid tracking number
  - _Show tracking history_
    - Display detailed tracking results for given tracking number
  - _Exit_
    - Exit program

#### _Enter new tracking number_ 

- Request tracking number from user
  - Check that tracking number has actually been entered
    - If no input has been given, continue to request until entered
  - Convert input into upper case to match expected format in Australia Post database
- Pass information back to menu
  - This function needs to pass the tracking number back to the menu function so that the user can see the active tracking number at the top of the menu

#### _Show current status_

- If user passes tracking number as argument to program:
  - Send tracking number to API
  
  - Check against Australia Post database with following possible responses:
  
    |Code|Name|Description|
    |-------|--------|---------------|
    |200|OK|Success|
    |400|Bad request|The request included bad syntax or bad request framing; or used deceptive routing.|
    |401|Unauthorised|Valid identity credentials were not provided in the request.|
    |403|Forbidden|You do not have sufficient permissions to access the resource.|
    |429|Too many requests|You sent too many requests to the same API endpoint within a specific time period. (See rate limiting for the specific endpoint.)|
    |500|Internal server error|Something unexpected has occurred on the server, and no other (more precise) status message is suitable.|
    |502|Bad gateway|The server you contacted was acting as a gateway or proxy and received an invalid response from an upstream server.|
    |503|Service unavailable|The server is unavailable due to maintenance, overload or an error state of some kind.|
    
  - Check if request returned OK
  
  - If valid, return most recent tracking update straight to command line and break



- If user did not pass tracking number as argument to program:
  - Inform user of option for future use to pass tracking number as argument to receive most recent tracking update at command line
  - Display menu giving user option to enter tracking number, which will be displayed at the top as active tracking number

#### _Display results_

- API returns information in JSON 
- Sample JSON return:
- {
    "tracking_results": [
      {
        "tracking_id": "7XX1000",
        "errors": [
          {
            "code": "ESB-10001",
            "name": "Invalid tracking ID"
          }
        ]
      },
      {
        "tracking_id": "7XX1000634011427",
        "status": "Delivered",
        "consignment": {
          "events": [
            {
              "location": "MEL",
              "description": "Item Delivered",
              "date": "2017-09-18T14:35:07+10:00"
            },
            {
              "location": "MEL",
              "description": "On Board for Delivery",
              "date": "2017-09-18T09:50:05+10:00"
            }
          ],
          "status": "Delivered in Full"
        },
        "trackable_items": [
          {
            "article_id": "7XX1000634011427",
            "product_type": "eParcel",
            "events": [
              {
                "location": "ALEXANDRIA NSW",
                "description": "Delivered",
                "date": "2014-05-30T14:43:09+10:00"
              },
              {
                "location": "ALEXANDRIA NSW",
                "description": "With Australia Post for delivery today",
                "date": "2014-05-30T06:08:51+10:00"
              },
              {
                "location": "CHULLORA NSW",
                "description": "Processed through Australia Post facility",
                "date": "2014-05-29T19:40:19+10:00"
              },
              {
                "location": "SYDNEY (AU)",
                "description": "Arrived at facility in destination country",
                "date": "2014-05-29T10:16:00+10:00"
              },
              {
                "location": "JOHN F. KENNEDY APT\/NEW YORK (US)",
                "description": "Departed facility",
                "date": "2014-05-26T05:00:00+10:00"
              },
              {
                "location": "JOHN F. KENNEDY APT\/NEW YORK (US)",
                "description": "Departed facility",
                "date": "2014-05-26T05:00:00+10:00"
              },
              {
                "description": "Shipping information approved by Australia Post",
                "date": "2014-05-23T14:27:15+10:00"
              }
            ]
          }
        ]
      }
    ]
  }
  HTTP Response Code: 200


- Information needs to be presented to user in a readable way upon successful retrieval
  
- If user has passed tracking number as argument:
  
  - Get most recent tracking event from JSON
    - Print most recent tracking event to screen in terminal
    - quit program 

#### _Show tracking history_

- Parse information from JSON
- Separate detailed tracking history available in another section of JSON file
  - Print this more detailed information presentably inside application



## User Interaction Outline

This program has been revised extensively to minimise UX frustrations, during development a number of areas were identified when running the program without an argument that needed improvement, and were iterated on until these frustrations had been removed.

1. Enter tracking number
   - Please enter your tracking number: 

2. Show current status
   - Prints most recent tracking event
- This option originally had a prompt for the user to enter a tracking number, had they not already done so before selecting it, but the user would then need to select option 2 again from the menu to execute the function.
   - Identifying this as a frustrating UX element, now, instead, they will be prompted to enter a number, after which point, the code for this function will execute automatically, the same as if they had entered a tracking number before selecting it.
   
3. Show detailed history
   - Prints full tracking history
- Like option 2, this option had the same issues regarding the input of a tracking number, but were more frustrating because option 3 required information derived from having run option 2 beforehand as well, thusly the user would have had to select 2, then 3, after having input the number.
   - Again, this was identified as a frustrating UX element, and has been revised to execute the code required to run the function correctly immediately after user enters tracking number.
   
4. Exit
   - Quits program, says Goodbye

## Control Flow Diagram

![Control Flow Legend](/docs/samuel-allen-T1A2-13-control-flow-legend.png)

![Control Flow Diagram](/docs/samuel-allen-T1A2-13-control-flow-diagram.png)



## Implementation Plan

| Feature                | Component                                                    | Priority                             | Timeframe | Completed |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------ | --------- | --------- |
| Create Menu            |                                                              | High                                 | 1hr       | 29/06/19  |
|                        | Stubbed menu - 1. Enter tracking number                      |                                      | 10-15min  | 29/06/19  |
|                        | Stubbed menu - 2. Show current status                        |                                      | 10-15min  | 29/06/19  |
|                        | Stubbed menu - 3. Show tracking history                      |                                      | 10-15min  | 29/06/19  |
|                        | Stubbed menu - 4. Exit                                       |                                      | 5min      | 29/06/19  |
|                        |                                                              |                                      |           |           |
| Refine Menu            |                                                              | Medium - depends on other functions  | 2-3hr     | 01/07/19  |
|                        | Argparse section to skip to set track_num variable and run show_tracking function if passed on run |                                      | 30min     | 29/06/19  |
|                        | Create track_num variable to show active tracking number     |                                      | 10-15min  | 29/06/19  |
|                        | Create error_response variable to show any current errors    |                                      | 10-15min  | 29/06/19  |
|                        | Create track_response variable to store and pass data between functions |                                      | 10-15min  | 29/06/19  |
|                        | Make option 1 call a function to input tracking number instead of a stub |                                      | 10-15min  | 29/06/19  |
|                        | Make option 2 call a function to show recent tracking event instead of astub, check if there is a tracking number present for the function to work, and if not, get user to input tracking number and run function |                                      | 10-15min  | 29/06/19  |
|                        | Make option 3 call a function to show tracking history instead of a stub, check for the presence of a tracking number, and the information from option 2 that is also required to run the function, if neither or partial, run those functions as required to get info before running function |                                      | 10-15min  | 29/06/19  |
|                        | Make option 4 quit the program instead of a stub             |                                      | 5min      | 29/06/19  |
|                        |                                                              |                                      |           |           |
| JSON-server            | Make JSON-server to host example GET responses as Australia Post will not give me an API key. | Low                                  | 1hr       | 29/06/19  |
|                        |                                                              |                                      |           |           |
| track_num function     |                                                              | High, needed to fully implement menu | 1-2hr     | 01/07/19  |
|                        | Request user input                                           |                                      |           | 29/06/19  |
|                        | Check input has been given (later changed to while loop 05/07/19) |                                      |           | 05/07/19  |
|                        | Change input to upper case                                   |                                      |           | 01/07/19  |
|                        | Reset error_response                                         |                                      |           | 01/07/19  |
|                        | Return error_response and track_response values to calling function |                                      |           | 01/07/19  |
|                        |                                                              |                                      |           |           |
| show_tracking function |                                                              | High, needed to fully implement menu | 4-5hr     |           |
|                        | Set URL for GET request                                      |                                      | 30min     | 01/07/19  |
|                        | Set required headers for GET request                         |                                      | 30min     | 01/07/19  |
|                        | Send GET request + track_num                                 |                                      | 30min     | 01/07/19  |
|                        | Check if return code is 200 OK                               |                                      | 15min     | 01/07/19  |
|                        | Search return text for tracking number                       |                                      | 30min     | 01/07/19  |
|                        | Parse JSON data to print the most recent tracking event to screen |                                      | 60min     | 01/07/19  |
|                        | Store JSON data in variable to return value for use in other function |                                      | 30min     | 01/07/19  |
|                        | Reset error_response                                         |                                      | 10min     | 01/07/19  |
|                        | Return error_response and track_response values to calling function |                                      | 30min     | 01/07/19  |
|                        |                                                              |                                      |           |           |
|                        | If tracking number is invalid, set error_response to display the error code received from the GET request and pass value to menu for display as current error |                                      | 10min     | 01/07/19  |
|                        |                                                              |                                      |           |           |
| show_history function  |                                                              | High, needed to fully implement menu | 1-2hr     | 03/07/19  |
|                        | Check that error_response is None and that track_response is not None |                                      | 10-15min  | 03/07/19  |
|                        | Use pprint to print the detailed tracking history of track_response |                                      | 1hr       | 03/07/19  |
|                        |                                                              |                                      |           |           |
|                        | Otherwise, return the passed error_response value to menu for display as current error |                                      | 10-15min  | 03/07/19  |


