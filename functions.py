#functions
import csv
def main():
    pass


def display_Data():

    with open("annual-co2-emissions-per-country.csv","r") as file:
        file.readline()
        count=0
        for line in file:
            count+=1
            parts=line.strip().split(",") #parts[0]=> country name  parts[1]=>country code  parts[2]=>year  parts[3]=>emission
            country=parts[0]
            year=parts[2]
            emission=parts[3]
            if parts[1]=="":
                country_Code=None




if __name__=="__main__":
    main()