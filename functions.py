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

if __name__=="__main__":
    main()
    display_Data()