#main.py
import functions

def main():
    data = functions.load_emission_data("annual-co2-emissions-per-country.csv")
    population_data = functions.load_population_data("population.csv")
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
13)Highest İncrease And Decrease in Emissions
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
            year = int(input("Yıl: "))
            threshold = float(input("Eşik değer (ton): "))
            result = functions.countries_above_threshold(data, year, threshold)
            for country, emission in result:
                print(f"{country}: {emission}")
        elif operation=="6":
            year = int(input("Yıl: "))
            c1 = input("1. Ülke: ")
            c2 = input("2. Ülke: ")
            diff = functions.country_comparison(data, year, c1, c2)
            print(f"{c1} ve {c2} arasındaki fark: {diff}")
        elif operation=="7":
            year = int(input("Yıl: "))
            min_val = float(input("Alt sınır (ton): "))
            max_val = float(input("Üst sınır (ton): "))
            functions.countries_in_range(data, year, min_val, max_val)
        elif operation=="8":
            country = input("Ülke: ")
            y1 = int(input("1. yıl: "))
            y2 = int(input("2. yıl: "))
            diff, percent = functions.year_to_year_comparison(data, country, y1, y2)
            print(f"Fark: {diff}, Yüzde değişim: %{percent:.2f}")
        elif operation=="9":
            country = input("Ülke: ")
            start = int(input("Başlangıç yılı: "))
            end = int(input("Bitiş yılı: "))
            avg = functions.average_emission(data, country, start, end)
            print(f"{country} için ortalama emisyon: {avg}")
        elif operation=="10":
            country = input("Ülke: ")
            year = int(input("Yıl: "))
            intensity = functions.emission_intensity(data, population_data, country, year)
            print(f"{country} ({year}) kişi başı emisyon: {intensity}")
        elif operation=="11":
            country = input("Ülke: ")
            trend = functions.trend_last_3_years(data, country)
            print(f"Trend (son 3 yıl): {trend}")
        elif operation=="12":
            country = input("Ülke: ")
            start = int(input("Başlangıç yılı: "))
            end = int(input("Bitiş yılı: "))
            order = input("Sıralama (asc/desc): ")
            functions.sort_emissions(data, country, start, end, order)
        elif operation=="13":
            inc, dec = functions.biggest_changes(data)
            print(f"En büyük artış: {inc}")
            print(f"En büyük azalış: {dec}")

        elif operation=="14":
            country = input("Ülke: ")
            functions.generate_country_report(data, country)
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
