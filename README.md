# Basic Python Page Server (Redux)
## Author Info
Author: Kaleo

Contact: kaleom@uoregon.edu

## Description
This project hosts a webpage server on the port specified in the credentials file. 
The characters ".." and "~" are considered invalid, and will return http 403. 
A skeleton credentials file "credentials-skel.ini" is included.
 
The page serving functionality is implemented using Flask.
The project is set up to use Docker.
A Makefile is provided with the task "run" which builds a docker image called "image" and runs it


## Sources used:

I based my request and file handling logic off of my work from project 1.

For python documentation references: python docs

https://docs.python.org/

These sources were only used to check how certain python functions/language constructs work

For http header format reference:

https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages

For flask documentation reference: the flask documentation

https://flask.palletsprojects.com/en/3.0.x/