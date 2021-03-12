# responsipy
## Response Tool
https://github.com/JCBrown602/responsipy
Command line (*nix) tool that asks for URL and gets HEADERS
for that URL.

# Branching Strategy
v1.0.0  - Single URL, user input
v1.1.0  - Import URLs from TXT file and return responses, content-types
develop - Ready for testing
f.<name>- Feature
master  - Release (tested version)

# To Do / Ideas
* Add file handling
  * Use a dummy file with a few URLs
  * Read the lines/URLs from the file and run the getResponse() fx
* Check for port numbers
* GUI? Eventually...

- Big issue with local var response
  - Issue was global v. local vars in Python - ambiguity
  https://www.geeksforgeeks.org/global-local-variables-python/
