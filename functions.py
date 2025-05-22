#functions
import csv
import math
import matplotlib.pyplot as plt

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


#########################################################################

def read_emission_data(filename):
    emission_data = []
    with open(filename, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            parts = line.strip().split(",")
            if len(parts) < 4:
                continue
            country = parts[0]
            try:
                year = int(parts[2])
                emission = float(parts[3])
                emission_data.append((country, year, emission))
            except ValueError:
                continue
    return emission_data

def read_population_data(filename):
    population_data = []
    with open(filename, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            parts = line.strip().split(",")
            if len(parts) < 3:
                continue
            country = parts[0]
            try:
                year = int(parts[1])
                population = int(float(parts[2]))
                population_data.append((country, year, population))
            except ValueError:
                continue
    return population_data


#Analysis Functions
#1.
def countries_above_threshold(data, year, threshold):
    result = []
    for country, y, emission in data:
        if y == year and emission > threshold:
            result.append((country, emission))
    return result

#2.
def country_comparison(data, country1, country2, year):
    e1 = e2 = None
    for c, y, e in data:
        if c == country1 and y == year:
            e1 = e
        if c == country2 and y == year:
            e2 = e
    if e1 is not None and e2 is not None:
        return abs(e1 - e2)
    return None

#3.
def countries_in_range(data, year, min_emission, max_emission):
    result = []
    for country, y, e in data:
        if y == year and min_emission <= e <= max_emission:
            result.append((country, e))
    return result

#4.  
def plot_emission_bar_chart(data):
    countries = [x[0] for x in data]
    emissions = [x[1] for x in data]
    plt.figure(figsize=(10, 5))
    plt.bar(countries, emissions)
    plt.xticks(rotation=90)
    plt.ylabel("CO2 Emisyonu")
    plt.title("Emisyon Aralığına Göre Ülkeler")
    plt.tight_layout()
    plt.show()


#5.
def year_to_year_comparison(data, country, year1, year2):
    e1 = e2 = None
    for c, y, e in data:
        if c == country and y == year1:
            e1 = e
        if c == country and y == year2:
            e2 = e
    if e1 is not None and e2 is not None:
        diff = e2 - e1
        percent = (diff / e1) * 100 if e1 != 0 else None
        return diff, percent
    return None

#6.
def average_emission(data, country, start_year, end_year):
    emissions = [e for c, y, e in data if c == country and start_year <= y <= end_year]
    if emissions:
        return sum(emissions) / len(emissions)
    return None

#7.
def emission_intensity(emission_data, population_data, country, year):
    e = p = None
    for c, y, val in emission_data:
        if c == country and y == year:
            e = val
            break
    for c, y, val in population_data:
        if c == country and y == year:
            p = val
            break
    if e is not None and p and p != 0:
        return e / p
    return None


#8.
def trend_last_3_years(data, country):
    records = [(y, e) for c, y, e in data if c == country]
    records.sort()
    if len(records) < 3:
        return None
    last3 = records[-3:]
    e1, e2, e3 = last3[0][1], last3[1][1], last3[2][1]
    if e1 < e2 < e3:
        return "Artış"
    elif e1 > e2 > e3:
        return "Azalış"
    else:
        return "Karışık"

#9.
def sort_emissions(data, country, start_year, end_year, ascending=True):
    records = [(y, e) for c, y, e in data if c == country and start_year <= y <= end_year]
    return sorted(records, key=lambda x: x[1], reverse=not ascending)

#10.
def biggest_changes(data, year1, year2):
    emissions = {}
    for c, y, e in data:
        if y == year1 or y == year2:
            if c not in emissions:
                emissions[c] = {}
            emissions[c][y] = e
    changes = []
    for c, years in emissions.items():
        if year1 in years and year2 in years:
            diff = years[year2] - years[year1]
            changes.append((c, diff))
    changes.sort(key=lambda x: x[1], reverse=True)
    return changes[:3], changes[-3:]

#11.report
def generate_country_report(data, country):
    records = [(y, e) for c, y, e in data if c == country]
    if not records:
        return None
    records.sort()
    years = [r[0] for r in records]
    emissions = [r[1] for r in records]
    min_all = min(emissions)
    max_all = max(emissions)
    last10 = emissions[-10:]
    min10 = min(last10)
    max10 = max(last10)
    avg10 = sum(last10) / len(last10)
    mean10 = avg10
    std10 = math.sqrt(sum([(x - mean10) ** 2 for x in last10]) / len(last10))
    return {
        "Yıllar": (years[0], years[-1]),
        "Tüm zaman en düşük": min_all,
        "Tüm zaman en yüksek": max_all,
        "Son 10 yıl en düşük": min10,
        "Son 10 yıl en yüksek": max10,
        "Son 10 yıl ortalama": avg10,
        "Son 10 yıl std sapma": std10
    }

def read_emission_data(filename):
    emission_data = []
    with open(filename, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            parts = line.strip().split(",")
            if len(parts) < 4:
                continue
            country = parts[0]
            try:
                year = int(parts[2])
                emission = float(parts[3])
                emission_data.append((country, year, emission))
            except ValueError:
                continue
    return emission_data

def read_population_data(filename):
    population_data = []
    with open(filename, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            parts = line.strip().split(",")
            if len(parts) < 3:
                continue
            country = parts[0]
            try:
                year = int(parts[1])
                population = int(float(parts[2]))
                population_data.append((country, year, population))
            except ValueError:
                continue
    return population_data


emission_data = read_emission_data("annual-co2-emissions-per-country.csv")
population_data = read_population_data("population.csv")

#########################################################################
if __name__=="__main__":
    main()
