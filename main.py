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
2)Display Data
3)Update Data
4)Delete Data
5)Countries Above Threshold
6)Country Comparison
7)Countries with Emissions in a Certain Range
8)Year-to-Year Comparison
9)Average Emission
10)Emission Intensity
11)Trend Analysis Over Time
12)Sorting Emission Data
13)Highhest İncrease And Decrease in Emissions
14)Report Generation                                     
If you want to quit enter Q or q""")
        operation=input("Your answer:")


        if operation.upper() == "Q":
            print("The program has been terminated")
            break
        elif operation not in ["1", "2", "3", "4", "5", "6", "7", "8","9","10","11","12","13","14"]:
            print("There is no such option, please enter again.")
            continue
         
        if operation=="1":
            functions.add_Data()
        elif operation=="2":
            functions.display_Data()
        elif operation=="3":       
            functions.update_Data()
        elif operation=="4":
            functions.delete_Data()
        elif operation=="5":
            pass
        elif operation=="6":
            pass
        elif operation=="7":
            pass
        elif operation=="8":
            pass
        elif operation=="9":
            pass
        elif operation=="10":
            pass
        elif operation=="11":
            pass
        elif operation=="12":
            pass
        elif operation=="13":
            pass
        elif operation=="14":
            pass
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
