#-------------------------------------------------------------------------------
# Name:        currentdate
# Purpose:     to display date and time seperating using datetime module
#
# Author:      surin
#
# Created:     22/08/2021
# Copyright:   (c) surin2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""two function  which is getter method is created which
return date and time respectively while casting it into string during
displaying it. this is done by importing datetime function
from standard library"""

#defining getDate() for date

def getDate():
    #importing datetime module for now()
    import datetime
    #using now() function to get current date and time and store in variable
    current_time = datetime.datetime.now()
    return str(current_time.date()) #casting object into string

#defining getTime() for time
def getTime():
    #importing datetime module for now()
    import datetime
    #using now() function to get current date and time and store in variable
    current_time=datetime.datetime.now()
    return str(current_time.time()) #casting object into string


