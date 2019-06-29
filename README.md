# CSB-SYD-19 A2 Terminal Application

### Australia Post delivery status

_aptrack TRACKINGNUMBERHERE_

The purpose of this application is for a user to be able to receive information regarding the status of a delivery from Australia Post, from the terminal, instead of having to utilise the Australia Post website to retrieve such information. It will retrieve the information via an HTTP GET request, utilising the Australia Post track/trace API, which will return information in JSON format, which will then be parsed and output to the user in a human readable form. This information will also be stored in a history file.

Being someone that finds themselves refreshing the Australia Post website constantly while waiting for a delivery, I feel that for a developer working in terminal frequently, it would be quite handy to have the ability to quickly get a status update from the command line instead of utilising the web page to retrieve this information.

The target audience for this application would be anyone awaiting a delivery from Australia Post that would like to receive information on the delivery status via the terminal, developers, or anyone using terminal frequently on a daily basis that receive postal deliveries. Perhaps employees in the mail department of a business or corporation that receive a lot of packages and utilise a terminal based workflow.

The application will be used as a command in terminal, with the package tracking number appended to the application command as an argument. This will then be checked for validity using the Australia Post API, if invalid, the user will be asked to input a valid tracking number, or have a choice to exit the application. If no argument is passed to the command line, the user will be asked to enter a number or have a choice to exit the application.

## Development Plan

### Features

#### _Retrieve tracking information_

- User passes tracking number as argument to program
  - Tracking number stored as **_variable_**
  
  - Variable checked against Australia Post database using API HTTP GET request, following possible responses:
  
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
    
  - Use try/except to make sure input consists of valid characters
  
  - Use loop to check if variable is returned as invalid, in order to ask user to enter a valid number or exit program
  
    - test against other fail conditions, break if response other than 200/400 received
    
    - limit on Australia Post API of 10 requests per minute, possibly implement this limit in program
    
      - HTTP header responses could be used for this purpose as follows:
    
        - X-RateLimit-Limit-hour: The maximum number of requests that the consumer is permitted to make per hour.
    
        - X-RateLimit-Remaining-hour: The number of requests remaining in the current rate limit window.
    
        - X-RateLimit-Limit-day: The maximum number of requests that the consumer is permitted to make per day.
    
        - X-RateLimit-Remaining-day: The number of requests remaining in the current rate limit window.
    
        - X-RateLimit-Limit-minute: The maximum number of requests that the consumer is permitted to make per minute.
    
        - X-RateLimit-Remaining-minute: The number of requests remaining in the current rate limit window.
    
        - X-RateLimit-Limit-second: The maximum number of concurrent requests that the consumer is permitted to make per second.
    
        - X-RateLimit-Remaining-second: The number of requests remaining in the current rate limit window.

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


  - Import JSON library
- Information needs to be presented to user on successful retrieval
  
  - Dump relevant JSON data into variables in human readable form
    - Print variables to screen in terminal
  - Possibly implement args in program to filter data from JSON to user preference, e.g. default is most recent status only, args could be set to show all tracking events from beginning 

#### _Store information in file_

- Store parsed information in text file

  - Alternatively, store all info before parsing to user for later use as whole data

    

- Append information from each run to form a history of queries and results

  - Possibly implement an option to import file from previous runs to show history in program
  
    

## User Interaction Outline

User will run program as described at the top of this file

