# Stock Data Project

Stock Data Project is a [python app] to consult Stock share price using JSON to collect data from Twelve Data API.

## Features

Once you start the app, you can input the symbol of the stock and the app will consult if is a valid Symbol Stock the app will store on the list and show Symbol high price and name of stock.

## Technologies

- Python
  - The main language used to build this app.
- GitHub
  - Source code is hosted on GitHub and delpoyed using Git Pages.
- Git
  - Used to commit and push code during the development opf the Website.
- Visual Studio Code IDE
  - The code was developed using Visual Studio Code IDE
- Twelve Data API
  - The Twelve data API used to access world financial markets including stocks, forex, ETFs, indices, and cryptocurrencies, free plan is possible to get 800 credits a day (max. 8 per minute) without cost. <https://twelvedata.com/docs#getting-started> and Pricing <https://twelvedata.com/pricing>

## Testing

### Responsiveness

The app was tested using the local terminal and heroku.com terminal

Steps to test:

1. Open browser to run on heroku terminal [Stock Data Project](https://stock-data-project-python-b57ee92c73ff.herokuapp.com) or use the link <https://github.com/JRakau/stock-data-project>
2. Click on RUN PROGRAM
3. Input the symbol of the stock do you want to checkout E.G. AAPL Apple Inc. or MSFT Microsoft Corporation.
4. App will validate the symbol and consult using the API
5. Once everything is right the app store results in a List to show on the terminal screen.
6. Once you finished you can use 'q' ou 'quit' to quit

#### Expected:

```
$ #############################
$ #                           #
$ #  Welcome to My Stocks     #
$ #                           #
$ #############################
$
$
$
$
$ Enter your ticker symbol here: (Or enter "quit(q)" to leave)
$ AAPL
```

```
$
$ ##########################################################
$ AAPL 176.49500 Apple Inc
$ ##########################################################
$
$ Enter another ticker symbol here: (Or enter "quit(q)" to leave)
$
```

#### Actual:

```
$ #############################
$ #                           #
$ #  Welcome to My Stocks     #
$ #                           #
$ #############################
$
$
$
$
$ Enter your ticker symbol here: (Or enter "quit(q)" to leave)
$ MSFT
```

```
$
$ ##########################################################
$ MSFT 337.39749 Microsoft Corp
$ ##########################################################
$
$ Enter another ticker symbol here: (Or enter "quit(q)" to leave)
$
```

### Pages Testing

#### Welcome screen

```
$ #############################
$ #                           #
$ #  Welcome to My Stocks     #
$ #                           #
$ #############################
$
$
$
$
$ Enter your ticker symbol here: (Or enter "quit(q)" to leave)
$
```

#### Adding Two Stock on the list

```
$ ##########################################################
$ AAPL 176.49500 Apple Inc
$ MSFT 337.39749 Microsoft Corp
$ ##########################################################
$
$ Enter another ticker symbol here: (Or enter "quit(q)" to leave)
$
```

#### Try to consult the ticker / Stock symbol does not exist

```
$ Fail: 400
$  Message: **symbol** not found: AABTC. Please specify it correctly according to API Documentation.
$ Try again please.
$
$
$
$
$ ##########################################################
$ AAPL 176.49500 Apple Inc
$ MSFT 337.39749 Microsoft Corp
$ ##########################################################
$
$ Enter another ticker symbol here: (Or enter "quit(q)" to leave)
$
```

#### Or it is included on different API pricing Plan

```
$ Fail: 400
$  Message: **symbol** BTC is not available with your plan. You may select the appropriate plan at https://twelvedata.com/pricing
$ Try again please.
$
$
$
$
$ ##########################################################
$ AAPL 176.49500 Apple Inc
$ MSFT 337.39749 Microsoft Corp
$ ##########################################################
$
$ Enter another ticker symbol here: (Or enter "quit(q)" to leave)
$
```

#### Leaving the app with q

```
$ Enter another ticker symbol here: (Or enter "quit(q)" to leave)
$ q
$
$
$
$
$ Thank you for using MyStock app. Hope see you again later
$
$
$
$
$
```

#### Or quit

```
$ Enter another ticker symbol here: (Or enter "quit(q)" to leave)
$ quit
$
$
$
$
$ Thank you for using MyStock app. Hope see you again later
$
$
$
$
$
```

## Deployment

### Version Control

The site was created using the Codeanywhere editor and pushed to github to the remote repository ‘weather-javascript-project’.

The following git commands were used throughout development to push code to the remote repo:

`git add <file>` - This command was used to add the file(s) to the staging area before they are committed.

`git commit -m “commit message”` - This command was used to commit changes to the local repository queue ready for the final step.

`git push` - This command was used to push all committed code to the remote repository on github.

### Deployment to Github Pages

- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the menu on left select 'Pages'
  - From the source section drop-down menu, select the Branch: main
  - Click 'Save'
  - A live link will be displayed in a green banner when published successfully.

The live link can be found here - <https://github.com/JRakau/stock-data-project>

### Deployment to Heroku

The live link can be found here - <https://stock-data-project-python-b57ee92c73ff.herokuapp.com>

### Clone the Repository Code Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now of been cloned on your local machine for use.
