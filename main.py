# main.py
import functions

def main():
    data = functions.read_emission_data("annual-co2-emissions-per-country.csv")
    population_data = functions.read_population_data("population.csv")

    print("\n--- Global CO2 Emissions Data System ---\n")

    answer = "Y"
    while answer.upper() == "Y":
        print("""
Which operation do you want to perform?
 1) Add Data
 2) Display Data
 3) Update Data
 4) Delete Data
 5) Countries Above Threshold
 6) Country Comparison
 7) Countries with Emissions in a Certain Range
 8) Year-to-Year Comparison
 9) Average Emission
10) Emission Intensity
11) Trend Analysis Over Time
12) Sorting Emission Data
13) Highest Increase And Decrease in Emissions
14) Report Generation
If you want to quit, enter Q or q
""")
        operation = input("Your choice: ").strip()

        if operation.upper() == "Q":
            print("The program has been terminated.")
            break

        if operation not in [str(i) for i in range(1, 15)]:
            print("Invalid option. Please try again.")
            continue

        try:
            if operation == "1":
                functions.add_Data()
            elif operation == "2":
                functions.display_Data()
            elif operation == "3":
                functions.update_Data()
            elif operation == "4":
                functions.delete_Data()
            elif operation == "5":
                year = int(input("Year: "))
                threshold = float(input("Threshold (tons): "))
                result = functions.countries_above_threshold(data, year, threshold)
                for country, emission in result:
                    print(f"{country}: {emission}")
            elif operation == "6":
                year = int(input("Year: "))
                c1 = input("1st Country: ")
                c2 = input("2nd Country: ")
                diff = functions.country_comparison(data, year, c1, c2)
                print(f"Difference between {c1} and {c2}: {diff}")
            elif operation == "7":
                year = int(input("Year: "))
                min_val = float(input("Minimum (tons): "))
                max_val = float(input("Maximum (tons): "))
                result = functions.countries_in_range(data, year, min_val, max_val)
                for country, emission in result:
                    print(f"{country}: {emission}")
            elif operation == "8":
                country = input("Country: ")
                y1 = int(input("First year: "))
                y2 = int(input("Second year: "))
                diff, percent = functions.year_to_year_comparison(data, country, y1, y2)
                print(f"Difference: {diff}, Percentage change: %{percent:.2f}")
            elif operation == "9":
                country = input("Country: ")
                start = int(input("Start year: "))
                end = int(input("End year: "))
                avg = functions.average_emission(data, country, start, end)
                print(f"Average emission for {country}: {avg}")
            elif operation == "10":
                country = input("Country: ")
                year = int(input("Year: "))
                intensity = functions.emission_intensity(data, population_data, country, year)
                print(f"{country} ({year}) per capita emission: {intensity}")
            elif operation == "11":
                country = input("Country: ")
                trend = functions.trend_last_3_years(data, country)
                print(f"Trend (last 3 years): {trend}")
            elif operation == "12":
                country = input("Country: ")
                start = int(input("Start year: "))
                end = int(input("End year: "))
                order = input("Sort order (asc/desc): ").lower()
                result = functions.sort_emissions(data, country, start, end, order)
                for year, emission in result:
                    print(f"{year}: {emission}")
            elif operation == "13":
                inc, dec = functions.biggest_changes(data,2013,2023)
                print(f"Largest increase: {inc}")
                print(f"Largest decrease: {dec}")
            elif operation == "14":
                country = input("Country: ")
                functions.generate_country_report(data, country)

        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
        except KeyError as e:
            print(f"Data error: {e}. Please check your input.")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Prompt to continue
        answer = input("Would you like to perform another operation? (y/n): ").strip()
        while answer.upper() not in ["Y", "N"]:
            answer = input("Please enter only 'y' or 'n': ")

        if answer.upper() == "N":
            print("The program has been terminated.")

if __name__ == "__main__":
    main()
