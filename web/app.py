"""
John Doe's Flask API.
"""

import config    # Configure from .ini files and command line
import os #to help with reading files

from flask import Flask

app = Flask(__name__)

#status codes for errors
#to avoid having magic numbers in code
STATUS_OK = 200
STATUS_FORBIDDEN = 403
STATUS_NOT_FOUND = 404

#list of forbidden strings
FORBIDDEN_STRINGS = {"..","~"}

#according to Flask documentation, this only handles
#get requests by default
@app.route("/<path:subpath>")
def hello(subpath):
    return getResponse(subpath)
    #return ("UOCIS docker demo!\n subpath: " + subpath + "\n port: " + str(get_options().PORT))


def getResponse(path):
    """
    Returns the contents at the provided path, and an HTTP status code.
    Checks to ensure the path is valid, and returns a 403 or 404 error page if necessary.
    Adapted from my solution to project 1
    """
    #ensure path is legal
    for forbidden in FORBIDDEN_STRINGS:
        if forbidden in path:
            return getErrorPage(STATUS_FORBIDDEN),STATUS_NOT_FOUND

    #find file and respond, or show 404 error page if not found
    completeFilePath = get_full_path(path)
    try:
        response = None
        with open(completeFilePath) as file:
            #transmit file
            response = ""
            lines = file.readlines()
            for line in lines:
                response += line
        return response, STATUS_OK
    except:
        return getErrorPage(STATUS_NOT_FOUND), STATUS_NOT_FOUND

def getErrorPath(errorCode):
    """
    Returns the path to the error page that should be loaded for a given error code
    """
    if not isinstance(errorCode,int):
        return "404.html"
    return str(errorCode) + ".html"

def getErrorPage(path):
    """
    Loads an error page from the path provided, and does not return a status code.
    If the page fails to load, returns a hardcoded error message to prevent further issues.
    If the provided value is an integer, converts it to the default error page for that http status automatically
    """
    
    if isinstance(path,int):
        path = getErrorPath(path)
    
    completeFilePath = get_full_path(path)
    #try:
    if True:
        response = None
        with open(completeFilePath) as file:
            #transmit file
            response = ""
            lines = file.readlines()
            for line in lines:
                response += line
        return response
    #except:
        #return "Exception while loading error page! You should never see this message!"

def get_full_path(filePath):
    """Returns the exact path to a page file, given the path from the docroot

    Just appends docroot to the current working directory, and then appends the file path to that
    """
    return os.path.join(os.getcwd(),get_docroot(),filePath)

def get_docroot():
    """
    Returns the path to use as the docroot path. 
    """
    #should always be pages according to the specs for this assignment
    return "pages"


def get_options():
    """
    Options from command line or configuration file.
    Returns namespace object with option value for port
    Taken from project 1 skeleton code
    """
    # Defaults from configuration files;
    #   on conflict, the last value read has precedence
    options = config.configuration()
    # We want: PORT, DOCROOT, possibly LOGGING

    if options.PORT <= 1000:
        log.warning(("Port {} selected. " +
                         " Ports 0..1000 are reserved \n" +
                         "by the operating system").format(options.port))

    return options


if __name__ == "__main__":
    app.run(debug=get_options().DEBUG, host='0.0.0.0', port = get_options().PORT)
