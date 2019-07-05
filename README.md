## aptrack

Compiled application located in dist folder

**_usage:_** App can be run with or without an argument provided, as follows

```
aptrack -t 7XX1000634011427
```

Will check the tracking number, then return the most recent tracking event recorded against it, printing both to the command line and then exiting.

Valid tracking numbers for the hosted examples are 7XX1000634011427 and 6XXX12345678

```
aptrack
```

Running the application with no argument provided will offer you a menu with 4 choices

1. Enter tracking information
2. Show current status
3. Show tracking history
4. Exit

If you select options 2 or 3 without entering a tracking number, you will be prompted to enter a number before those functions will execute.

Option 2 will return the most recent tracking event recorded against the tracking number, as well as updating the menu display with any errors returned while checking

Option 3 will return a detailed history of all the tracking events recorded against the tracking number, and will also update the menu display with any errors returned while checking.

Option 4 will exit the program.


