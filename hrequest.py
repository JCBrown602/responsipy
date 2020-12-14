# Response Tool
# Content-Type, Port Number

# Import requests module
import requests
# probably need a file i/o module

# Vars
# url file, response
url = 'https://example.com'
response = requests.get(url)

# User input for url file name OR url
print("Enter something: ", end = '')
input1 = input()

# Loop through url.txt/url and print Content-Type
def responseLoop():
    print("RESPONSE: ", response)
    print("HEADERS: ", response.headers)

# IF logic
if input1 is not None:
    # if user entered url, treat it as a single "url"
    response = requests.get(input1)
    print("Single URL: ", input1)
    responseLoop()
else:
    # if user entered file, treat it as a "url.txt"
    # Open and read url.txt to var
    responseLoop()
