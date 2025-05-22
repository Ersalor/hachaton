#functions
import csv
def main():
    pass
############################################################
def turkish_lower(text):
    return text.replace("I","ı").replace("İ","i").lower()
############################################################


def display_Data():
    
    print("Listing Types;\n"
        "1)Listing data for a specific year\n"
        "2)Listing data for a specific country\n"
        "3)Listing data for a specific CO2 emission range\n")
    list_Type=input("Please select the listing type:").strip()
    print()
    while list_Type not in ["1","2","3"]:
        list_Type=input("Enter a valid option(1,2,3):").strip()
        print()
    if list_Type=="1":
        try:
            input_year=int(input("Which year do you want to display?:"))
            print()
        except ValueError:
            print("You didn't enter a valid number")
            print("Program has been terminated")
            return
        
    elif list_Type == "2":
        valid_countries = set()
        with open("annual-co2-emissions-per-country.csv", "r") as file:
            file.readline()
            for line in file:
                parts = line.strip().split(",")  
                valid_countries.add(parts[0].lower())
        while True:
            input_country = input("Which country do you want to display?: ").strip()
            converted_input_country=turkish_lower(input_country)
            if converted_input_country in valid_countries:
                break
            print("This country is not found in the data. Please enter a valid country name.")
   
    ############################################################
    elif list_Type == "3":
        try:
            min_emission = float(input("Enter minimum CO2 emission value: ").strip())
            max_emission = float(input("Enter maximum CO2 emission value: ").strip())
            print()
        except ValueError:
            print("You didn't enter a valid number.")
            print("Program has been terminated")
            return
    ############################################################

    
    with open("annual-co2-emissions-per-country.csv","r") as file:
        country_list=[]
        # year_list=[]
        # country_code_list=[]
        # emission_list=[]
        file.readline()
        country_counter=0
        count=0
        for line in file:
            count+=1
            parts=line.strip().split(",") #parts[0]=> country name  parts[1]=>country code  parts[2]=>year  parts[3]=>emission
            country=parts[0]
            year=int(parts[2])
            emission=float(parts[3])
            if len(parts[1])==0:
                country_Code="None"
            else:
                country_Code=parts[1]
            if list_Type=="1" and input_year==year:
                country_list.append([country,country_Code,emission])
            if list_Type=="2" and converted_input_country==country.lower(): 
                country_list.append([year,emission])
            ############################################################
            if list_Type=="3" and min_emission <= emission <= max_emission:
                country_list.append([country, country_Code, year, emission])
            ############################################################

    if list_Type=="1":
        i=0
        while i<len(country_list):
            if count==1:
                print(f"Annual CO2 emissions in {input_year}:")
            print(f"{country_list[i][0]}({country_list[i][1]}) => {country_list[i][2]}")
            country_counter+=1
            i+=1
    elif list_Type=="2":
        i=0
        while i<len(country_list):
            if count==1:
                print(f"Annual CO2 emissions in {input_country.capitalize()}:")
            print(f"{country_list[i][0]} => {country_list[i][1]}")
            country_counter+=1
            i+=1
    
    ############################################################
    elif list_Type=="3":
        i = 0
        print(f"Countries with CO2 emission between {min_emission} and {max_emission}:")
        while i < len(country_list):
            print(f"{country_list[i][0]} ({country_list[i][1]}) in {country_list[i][2]} => {country_list[i][3]}")
            country_counter+=1
            i+=1
    ############################################################

    if list_Type=="1":
        print(f"{country_counter} country ")
    elif list_Type=="2":
        print(f"{country_counter} result found")
    elif list_Type=="3":
        print(f"{country_counter} result found")
    else:
        pass


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
