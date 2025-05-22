#main.py
import functions

def main():
    print()
    print("---Global CO2 Emissions Data System---\n")
    answer="Y"
    count=0
    while answer.upper()=="Y":
        count+=1
        print("""Which operation do you want to perform?
1)Add Data
2)Listing
3)Adding
4)Deleting
5)Updating
6)Moving Records
7)Plotting Graphics
8)Analyzing
If you want to quit enter Q or q""")
        operation=input("Your answer:")


        if operation.upper() == "Q":
            print("The program has been terminated")
            break
        elif operation not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("There is no such option, please enter again.")
            continue
         
        if operation=="1":
            functions.search_Neighborhoods()
        elif operation=="2":
            functions.list_Neighborhoods()
        elif operation=="3":       
            functions.add_Neighborhoods()
        elif operation=="4":
            functions.delete_Neighborhoods()
        elif operation=="5":
            functions.update_Neighborgoods() #add fonksiyonundan sonra açılacak
        elif operation=="6":
            functions.move_Neighborhoods()  #add fonksiyonundan sonra açılacak
        elif operation=="7":
            print("You choose operation 7")
        elif operation=="8":
            print("You choose operation 8")
        elif operation.upper()=="Q":
            print("The program has been terminated")
            break
      
        if(count>0):
            answer=input("Would you like to perform another operation?(y/n):")
            while answer.upper()!="Y" and answer.upper()!="N":
                answer=input("Please Enter only y or n:")

            if(answer.upper()!="Y"):
                print("The program has been terminated")


if __name__=="__main__":
    main()
