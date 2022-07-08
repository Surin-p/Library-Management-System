#-------------------------------------------------------------------------------
# Name:       CollectionSplit
# Purpose:this module contain a function named splitCollection read the bookcollection
#   txt file which is then splited into the different 2Dlists as data structure
#according to requirements.
# Author:      Surin
#
# Created:     20/08/2021
# Copyright:   (c) surin2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""this module contain a function named splitCollection read the bookcollection
txt file which is then splited into the different 2D lists according to requirements."""


#defining function with no parameters

def splitCollection():
    #defining global variable
    global kbookName
    global bauthorName
    global kbookQuantity
    global klibraryPrice
    global kbookIsbn
    global kbookGenre

    # empty lists
    kbookName = []
    bauthorName = []
    kbookQuantity = []
    klibraryPrice = []
    kbookIsbn = []
    kbookGenre = []

    #initializing f to read data from text file
    f = open("bookcollection.txt","r")
    lines = f.readlines()  #read each lines from file and initialized in list
    lines = [x.strip() for x in lines] #remove line breaks and store in line as list



    for i in range(len(lines)):

        index = 0 #internal counter

        for l in lines[i].split(","):  #sperating content by ,

            if(index==0): #for first element of textfile which at o index in list
                kbookName.append(l.strip()) #adding to list and strip unwanted things
                
                
            elif(index==1):  #for second element of text file
                bauthorName.append(l.strip())

            elif(index==2):
                kbookQuantity.append(int(l))

            elif(index==3):
                #removing $
                p = l.strip("$")
                klibraryPrice.append(p)

            elif(index==4):
                kbookIsbn.append(l)

            elif(index==5):
                kbookGenre.append(l)

            index+=1

    f.close()





splitCollection()


