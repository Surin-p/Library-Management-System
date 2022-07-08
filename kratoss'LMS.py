"""this module is main module of our library which implement other module
and their functions seperately  for different operation as user input, reading
files, borrowing or returning."""


#importing required module
import CollectionSplit as cs
import currentdate as cd
import lendBook as l
import giveBack as gB

#defining function with no parameters for this module
def main():
    #working in loop
    loop = True
    while (loop == True):
        print("                 Kratoss' Library                   ")
        print("        Welcome to Library Management System        ")
        print("Date: " + cd.getDate() + "          Time:"+ cd.getTime())
        print("")
        print("(>.<)" *10)
        print("To see collection of our books-->Press 1")
        print("To borrow any book------->Press 2")
        print("To return the book------->Press 3")
        print("To do nothing #exist----->Press 4")
        print("(>.<)" *10)
        print("")

        #exception handling for value error
        try:
            pick = int(input("Please Select and press only from the choice mentioned above i.e 1-4: "))
            print("")

            if (pick==1):
                f = open("bookcollection.txt","r") #read mode only
                lines = f.read()
                print(lines + "\n")
                print()
                f.close()


            elif(pick==2):

                cs.splitCollection() #calling function to initialize global list
                l.lendBook() #calling lendBook from lend module

            elif(pick==3):

                cs.splitCollection()
                gB.giveBook()

            elif(pick==4):

                print("Thank for using service from Krotoss' Library O_O")
                break #stop loop

            else:
                print("Told u before press number only from 1-4")

        except ValueError:
            print("Choose wisely :<")

# run program
main()
