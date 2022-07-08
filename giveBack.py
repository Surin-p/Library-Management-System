#-------------------------------------------------------------------------------
# Name:        giveBack
# Purpose: function returnBook is created and then the price is calculated for book
# and seen if the book lend exceed the day
# Author:      acer
#
# Created:     27/08/2021
# Copyright:   (c) surin2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#importing required module
import currentdate as cd
import CollectionSplit as cs


#defining function for returning book and price calculation
def giveBook():

    name = input("Enter the name of borrower: ")
    lend = "Borrower- "+name+".txt"
    #exception for name of borrower no found
    try:
        f = open(lend,"r") #read mode
        lines=f.readlines()
        lines=[lend.strip("$") for lend in lines]

        f = open(lend,"r")
        info = f.read()
        print(info)
    except:
        print("The borrower name is incorrect")
        giveBook()

    payBy = "Returner- "+name+".txt"
    #for returner note
    f = open(payBy,"w+") #read and write mode
    f.write("                    Kratoss' Library   \n        ")
    f.write("               Library Management System  \n     ")
    f.write("        Borrowed By: "+ name + "\n")
    f.write("    Date: " + cd.getDate()+"    Time:"+ cd.getTime()+"\n\n")
    f.write("___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ _" + "\n")
    f.write("\n")
    f.write("S.N. ||\t Name of Book||\t Author Name||\t Price of Book | \n")
    f.close()

    #float variable
    total = 0.0
    for g in range(8):
        list = cs.kbookName[g]
        if list in info:
            f = open(payBy, "a") #append
            f.write(str(g+1) +"|| \t "+ cs.kbookName[g]+"|| \t  "+cs.bauthorName[g]+" || \t  "+cs.klibraryPrice[g]+" | "+"\n")
            cs.kbookQuantity[g] = cs.kbookQuantity[g] + 1
            f.close()


            total += float(cs.klibraryPrice[g])


    print("")
    print("Total price -------------------------------------->>>"+"$"+str(total))
    print("")
    print("Is the date of returning more than 10 days??")
    choosen = input("Press Y for Yes and N for No: ")
    if(choosen.upper()=="Y"):
        day=int(input("By how many days the book returned was late? "))
        fine=2*day

        f = open(payBy,"a")
        f.write("\t\t\t\t\tFine: $"+str(fine)+ "\n")
        f.close()
        total=total+fine
        print("")
        print("Oops u got to pay extra...:(")

    else:
        print("")
        print("Thank u for returning in time:)")

    print("")
    print("Final Total: "+ "$"+ str(total))


    f = open(payBy,"a")
    f.write("\t\t\t\t\tTotal: $"+ str(total) + "\n")
    f.close()

    with open("bookcollection.txt","w+") as f:
        for g in range(8):
            f.write(cs.kbookName[g]+","+cs.bauthorName[g]+","+str(cs.kbookQuantity[g])+","+"$"+cs.klibraryPrice[g]+","+cs.kbookIsbn[g]+","+cs.kbookGenre[g]+"\n")










