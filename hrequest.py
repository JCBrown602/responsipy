"""
Response Tool
https://github.com/JCBrown602/responsipy
Command line (*nix) tool that asks for URL and gets HEADERS
for that URL.

TODO:
 - Isolate Content-Type
 - Open text file containing URLs and get Content-Type for all of them
    - Could be 100+ URLs
 - Get port number? Available in requests module?
"""

# Import requests module
import requests
# probably need a file i/o module

# Vars
# url file, response
url = 'https://example.com'
response = requests.get(url)
strError = 'UNDEFINED'
input1 = 'Nothing'

# User input for url file name OR url
def getInput():
    global input1
    print("Enter something: ", end = '')
    input1 = input()
    checkInput(input1)
    return input1

def getResponse(input1):
    global response
    response = requests.head(input1)
    return response

def showMsg(strError):
    print("*** ", strError, ": Must enter a full URL starting with http:// or https:// ***")

# Error handling
def checkInput(input1):
    global response
    
    # 'is not None' doesn't catch an empty/blank string
    if input1:
        # if user entered url, treat it as a single "url"
        try:
            #response = requests.head(input1)
            response = getResponse(input1)
            #print("URL: ", response.url)
            #print("TRY: Response is currently: ", response)
            showResponse(response)
        except requests.exceptions.MissingSchema:
            strError = 'MissingSchema'
            showMsg(strError)
            getInput()
        except:
            strError = 'Bad'
            showMsg(strError)
            getInput()
    else:
        print("*** Something happened, but it was wonky. Try again. ***")
        getInput()
    #print("CHECKED input was: ", input1)
    #print("RETURN: Response is currently: ", response)
    return response

# Loop through url.txt/url and print Content-Type
def showResponse(response):
    print("-")
    print("URL: ", response.url)
    print("SERVER: ", response.headers['server'])
    print("RESPONSE: ", response.status_code)
    print("CONTENT-TYPE: ", response.headers['content-type'])
    print("-")

# IF logic
    # if user entered file, treat it as a "url.txt"
    # Open and read url.txt to var

# Start the loop
getInput()
