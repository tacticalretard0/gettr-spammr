# gettr-spammr
A bot that spams gettr.com

## Requirements
It mostly uses my own API but some of it requires [gogettr](https://github.com/stanfordio/gogettr)

## How to add an account
1. Put a file in the `tokens/` directory, name the file `token_username.txt`, where username is the username of the account you want to add

1. Put the account's token in the file you created

The account you added will automatically be used as a bot the next time spammr.py is run

### How to get an account's token
1. Log in to the account

1. Open your browser's developer tools (CTRL+Shift+I or F12)

1. Go to the network tab

1. While it is recording requests, create a post on gettr, the post can contain anything

1. Click on one of the requets named "post", there might be two of them, but the correct one is the one that says "Request Method: POST", the wrong one will say "Request Method: OPTIONS"

1. Scroll down to the request headers, find x-app-auth

1. x-app-auth should contain a json string like this `{"user": "username_here", "token": "token_here"}`, copy the value in "token", excluding the quotation marks

You should now have the token

