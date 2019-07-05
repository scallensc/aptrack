## Development Log

### 29/06/19

_Morning:_

Made a basic menu using a while true loop, planning to add functions for each menu option and add API key information once received from Australia Post.

James showed me how to install and run npm package JSON-server, as Australia Post has example JSON replies on their website, which allows me to get coding until I can access the actual production server.

![Trello board](/docs/samuel-allen-T1A2-13-project-management-1.png)

_Afternoon_:

Got JSON-server installed and working with sample responses provided on Australia Post website, stored in /jsondb.

Menu options added, implemented function to enter tracking number, tested GET request using python interpreter against local JSON-server, seems to work.

Basic argparse functionality in menu.

Added function to retrieve tracking info from JSON-server.

### 01/07/19

Morning:

Was having some difficulties for some reason remembering how to have a function return the data stored in a local variable into another function. Spent some time re-coding the menu, tracking number input and tracking status retrievals on my phone while at work just to confirm I remembered how to do from scratch, worked out I could declare a variable as global in order to have the information passed between functions.

![Phone coding](/docs/samuel-allen-T1A2-13-code_on_phone.png)

Afternoon:

Found Postman API testing system and created account there, added code to function to show tracking info to utilise Postman mock server.

Worked out how to return variable data from one function to another without using globals and removed all global variables from program, have implemented a check on the status code for the return from Postman, with an if condition to see if the return code is 200 OK or not.

More code for argparse section in order to have the program run correctly when argument passed on program run

### 03/07/19

Morning:

Implemented code to search the response for the tracking number entered in order to display results for that tracking number, as some of the Australia Post example responses contain partial or invalid tracking numbers because you can send multiple numbers to the API separated by commas.

Implemented code correctly to show the active tracking number that has been input in the menu, as well as any current error responses from the server.

argparse code will correctly run in_track function and then funnel result to track_result function, printing the output straight to the command line. If an error is received instead, it will print the response code.

Afternoon:

Implemented code to correctly print the most recent tracking event when selecting the tracking status function from the menu. Figured out how to have multiple variables returned from a single function by packing into tuple and then unpacking that tuple into variables in the function I need those values returned to.

Used pprint function to print dictionaries in a nicer readable form in order to implement the detailed tracking function when selected. Formatted code to better comply with pylint suggestions.

Have identified some UX issues, I had implemented functionality for instance when you select option 2 (show most recent tracking event) and there hasn't already been a tracking number entered, the program will enter the enter tracking number function, which will then set the active tracking number that option 2 needs to run properly, however you then have to select option 2 again to get the result, I want this to be done automatically after entering the tracking number.

### 04/07/19

Morning:

Worked out the issue I was having with the show_tracking and show_history functions not automatically running themselves after being selected before having input a tracking number. They now both ask for a tracking number to be entered if not present, and then execute the code that would have been executed, had a tracking number already been present.

Push as v0.2

App is mostly feature complete at this point, need to finish documentation and design tests.

Australia Post never replied with API key, so I have left code in that would retrieve info correctly from them with valid credentials, which is commented out in code.

![Trello](/docs/samuel-allen-T1A2-13-project-management-2.png)

Afternoon:

Updates to documentation, have also gone through code and removed recursion, replaced with While loop instead.

Created bash script to automate creation of executable
Ran bash script

![Trello](/docs/samuel-allen-T1A2-13-project-management-3.png)