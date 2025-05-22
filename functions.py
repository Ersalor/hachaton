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
            if len(parts[1])==0:
                country_Code=None
            else:
                country_Code=parts[1]

def add_Data(*,is_certain=False,adding_country,adding_code,adding_year,adding_carbon):
    while True:
        exist = False
        if is_certain == False:         
            add_country = input("Enter the country : ").strip().capitalize()
            add_code = input("Enter the code : ").strip().upper()
            add_year = input("Enter the year : ")
            add_carbon = input("Enter the carbon : ")

        else:
            add_country = adding_country
            add_code = adding_code
            add_year = adding_year
            add_carbon = adding_carbon

        solution = add_country + " " + add_year

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
                else:
                    country_Code = parts[1]
                control = country + " " + year 

                if solution == control:
                    print("Already exist")
                    exist = True
                    break

            if exist == False:
                solution = add_country + "," + add_code + "," + add_year + "," + add_carbon
                with open("annual-co2-emissions-per-country.csv","a") as adding:
                    adding.write("\n" + solution)
                print("Added")

def delete_Data(*,is_certain=False,deleting_country,deleting_year):

    while True:

        with open("annual-co2-emissions-per-country.csv", "r") as file:
            rows = file.readlines()

        if is_certain == False:  
            delete_country = input("Enter the country : ").strip().capitalize()
            delete_year = input("Enter the year : ")

        else:
            delete_country = deleting_country
            delete_year = deleting_year

        solution = delete_country + " " + delete_year
        found = False
        new_rows = []

        with open("annual-co2-emissions-per-country.csv","r") as file:
            file.readline()
            count=0
            for line in file:
                count+=1
                parts=line.strip().split(",") #parts[0]=> country name  parts[1]=>country code  parts[2]=>year  parts[3]=>emission
                country=parts[0]
                year=parts[2]
                control = country + " " + year 
                if solution == control :
                    print("silindi")
                    found = True
                    continue
                else:
                    new_rows.append(line)

            if found != False:
                with open("annual-co2-emissions-per-country.csv","w") as writer:
                    writer.writelines(new_rows)
                break
            else:
               print("not found")



def update_Data():

    while True:
        with open("annual-co2-emissions-per-country.csv","r") as reader:
            rows = reader.readlines()
        update_country = input("Enter the country : ").strip().capitalize()
        update_code = input("Enter the code : ")
        update_year = input("Enter the year : ")
        update_carbon = input("Enter the new CO2 : ")
        delete_Data(is_certain=True,deleting_country=update_country,deleting_year=update_year)
        with open("annual-co2-emissions-per-country.csv","r") as new_reader:
            new_rows = new_reader.readlines()

        if new_rows != rows:
            break
    
    add_Data(is_certain=True,adding_country=update_country,adding_code=update_code,adding_year=update_year,adding_carbon=update_carbon)
    print("updated")






if __name__=="__main__":
    main()
    