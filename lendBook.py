#-------------------------------------------------------------------------------
# Name:        lendBook
# Purpose:contain a function lendBook() to lend book and generates note also
# decreasing quantity from stocks
# Author:      Surin
#
# Created:     04/09/2021
# Copyright:   (c) surin 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#importing required packages
import CollectionSplit as cs
import currentdate as cd
def lendBook():

    #working in loop
    borrowed = False
    while(True):
        firstName = input("Enter your first name: ")
        if (firstName.isalpha()):
            break
        print("Enter valid first name")

    while(True):
        lastName = input("Enter your sur name: ")
        if (lastName.isalpha()):
            break
        print("Enter valid sur name")

    #making textfile for borrower note
    borrower = "Borrower- "+firstName+ ".txt"
    f = open(borrower,"w+") #open for read and write mode
    f.write("                 Kratoss' Library                  \n ")
    f.write("        Welcome to Library Management System        \n")
    f.write("\t\t\t"+"Lend to- "+ firstName+ "" + lastName +"\n")
    f.write("Date: " + cd.getDate() +"\t" "          Time:"+ cd.getTime() +"\n")
    f.write("___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ____  _____ _____" + "\n")
    f.write("\n")
    f.write("|S.N.  || \t Name of Book \t || \t AuthorName || \t Price of Book \t||\t Genre                 |"+"\n")


    while (borrowed==False):
        print("Please Select book from option below: ")
        for b in range (len(cs.kbookName)):
            print("Enter", b, "to borrow book", cs.kbookName[b])

        #exceptional handling
        #for value error exception
        try:
            choice = int(input())
            #for index error
            try:
                if (cs.kbookQuantity[choice]>0):
                    print("Thankfully book u needed is in our Collection :)")
                    f = open(borrower,"a") #append mode
                    f.write("|1.   "  +"  || \t"+ cs.kbookName[choice]+  "  ||     "+ cs.bauthorName[choice]+"||  \t"+  "  $"+cs.klibraryPrice[choice]+"  ||  "+cs.kbookGenre[choice] +"        |"+" \n")

                    cs.kbookQuantity[choice] = cs.kbookQuantity[choice]-1

                    f = open("bookcollection.txt","w")  #writing mode
                    for i in range(8):
                        f.write(cs.kbookName[i]+","+cs.bauthorName[i]+","+ str(cs.kbookQuantity[i])+","+"$"+cs.klibraryPrice[i]+","+cs.kbookIsbn[i]+","+cs.kbookGenre[i]+"\n")

                    loop = True
                    count = 1
                    while(loop==True):
                        cont = str(input("Do you want to continue to borrow (Y/N): "))
                        if (cont.upper()=="Y"):
                            count += 1
                            print("Please Select book from option below: ")
                            for b in range (len(cs.kbookName)):
                                print("Enter", b, "to borrow book", cs.kbookName[b])

                            choice = int(input())

                            if (cs.kbookQuantity[choice]>0):
                                print("Thankfully book u needed is in our Collection :)")

                                f = open(borrower,"a") #append mode
                                f.write("|"+str(count)+".    ||    "+ cs.kbookName[choice]+"    ||     "+ cs.bauthorName[choice]+" ||  \t"+"      "+"$"+cs.klibraryPrice[choice]+"  ||      \t"+cs.kbookGenre[choice] +"      |"+" \n")

                                cs.kbookQuantity[choice] = cs.kbookQuantity[choice]-1

                                f = open("bookcollection.txt","w")  #writing mode
                                for i in range(8):
                                    f.write(cs.kbookName[i]+","+cs.bauthorName[i]+","+ str(cs.kbookQuantity[i])+","+"$"+cs.klibraryPrice[i]+","+cs.kbookIsbn[i]+","+cs.kbookGenre[i]+"\n")

                                    borrowed= True


                            else:
                                loop=False
                                break

                        elif (cont.upper()=="N"):
                            print("Thank you for borrowing from us :)")
                            print("")
                            loop = False
                            borrowed = True

                        else:
                            print("Please choose as mentioned ^_^")

                else:
                    print("Sorry book is out of collection T_T")
                    lendBook()
                    borrowed = False

            except IndexError:
                print("")
                print("Please choose as instructed ^_^")

        except ValueError:
            print("")
            print("Choose wisely :)")






