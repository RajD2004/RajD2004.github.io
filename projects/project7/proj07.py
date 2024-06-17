import csv
from datetime import datetime
from operator import itemgetter

COLUMNS = ["date",  "average temp", "high temp", "low temp", "precipitation", \
           "snow", "snow depth"]

TOL = 0.02

BANNER = 'This program will take in csv files with weather data and compare \
the sets.\nThe data is available for high, low, and average temperatures,\
\nprecipitation, and snow and snow depth.'    


MENU = '''
        Menu Options:
        1. Highest value for a specific column for all cities
        2. Lowest value for a specific column for all cities
        3. Average value for a specific column for all cities
        4. Modes for a specific column for all cities
        5. Summary Statistics for a specific column for a specific city
        6. High and low averages for each category across all data
        7. Quit
        Menu Choice: '''
        
      
        
def open_files():
    #prompt user to enter a seires of cities, each followed by a comma 
    cities = input("Enter cities names: ").split(",")
    
    #Initialized empty lists for the valid cities and their corresponding file pointers 
    valid_cities = []
    file_pointers = []

    #iterate over the list of cities
    for city in cities:
        try:
            #try to open the csv file for the city
            file_pointer = open(city.strip()+"_small.csv",'r') 
            #if successful, add city to the list of valid cities 
            valid_cities.append(city.strip())
            #add the file pointer to the list of file pointers 
            file_pointers.append(file_pointer)
        except FileNotFoundError:
            #if the file is not found, the error message is printed 
            print(f"Error: File {city.strip()}.csv is not found")
    return valid_cities, file_pointers

'''def read_files(cities_fp):
    data = []
    for fp in cities_fp:
        f = open(fp, 'r')  
        f.readline()
        f.readline()
        rows = []
        for line in f:
            cols = line.strip().split(',')
            cols = [None if x == '' else x for x in cols]
            rows.append(tuple(cols))
        data.append(rows)
        f.close()
    return data '''

def read_files(cities_fp):
    def clean_row(row):
        cleaned_row = []
        for i, item in enumerate(row):
            item = item.strip()
            if i == 0:
                cleaned_row.append(item)
            else:
                cleaned_row.append(float(item) if item != '' else None)
        return tuple(cleaned_row)
        
    data = []
    for fp in cities_fp:
        fp_data = []
        for i, line in enumerate(fp):
            if i < 2:
                continue
            row = line.strip().split(',')
            fp_data.append(clean_row(row))
        data.append(fp_data)
        fp.close()
        
    return data

    
    


def get_data_in_range(master_list, start_str, end_str):
    
    start_date = datetime.strptime(start_str, "%m/%d/%Y").date()
    end_date = datetime.strptime(end_str, "%m/%d/%Y").date()
    filtered_data = []
    for lst in master_list:
        filtered_lst = []
        for tup in lst:
            date_str = tup[0]
            date = datetime.strptime(date_str, "%m/%d/%Y").date()
            if start_date <= date <= end_date:
                filtered_lst.append(tup)
        filtered_data.append(filtered_lst)
    return filtered_data
'''
def get_min(col, data, cities): 

    #finds the minimum value of the column with index col for the data in each city in the cities list
    #returns a list of tuples 

    def get_col_data(col_index, data):
        #helper function to extract column data from the list of tuples. 
        return [row[col_index] for row in data]
    
    result = []
    for city in cities:
        city_data = [row for row in data if row[-1] == city]
        if not city_data:
            continue
        city_col_data = get_col_data(col, city_data)
        city_min = min(city_col_data)
        result.append((city, city_min))
    return result 
'''
def get_min(col, data, cities):      
    def get_min_for_city(city_data):
        col_data = [row[col] for row in city_data if row[col] is not None]
        return min(col_data)

    result = []
    for i in range(len(cities)):
        city_data = [row for row in data[i] if row[1] is not None]
        min_value = get_min_for_city(city_data)
        result.append((cities[i], min_value))

    return result  
    
    
        
'''def get_max(col, data, cities): 
    
    #finds maximum value of the corresponding column col for each city in cities.
    #returns a list of tuples similar to the get_min() function

    def get_max_val(city_data):

        #helper function similar to the one made in get_min(), but finds max value
        return max(row[col] for row in city_data)
    
    result = []
    for city in cities:
        city_data = [row for row in data if row[-1] == city]
        if city_data:
            max_value = get_max_val(city_data)
            result.append((city, max_value))
    return result'''

def get_max(col, data, cities):
    def get_max_for_city(city_data):
        col_data = [row[col] for row in city_data if row[col] is not None]
        return max(col_data)

    result = []
    for i in range(len(cities)):
        city_data = [row for row in data[i] if row[col] is not None]
        max_value = get_max_for_city(city_data)
        result.append((cities[i], max_value))

    return result

'''def get_average(col, data, cities):
    def get_average_for_city(city_data):
        col_data = [row[col] for row in city_data if row[col] is not None]
        return sum(col_data) / len(col_data)

    result = []
    for i in range(len(cities)):
        city_data = [row for row in data[i] if row[1] is not None]
        average_value = get_average_for_city(city_data)
        result.append((cities[i], average_value))

    return result'''

def get_average(col, data, cities):
    def get_average_for_city(city_data):
        col_data = [row[col] for row in city_data if row[col] is not None]
        if not col_data:
            return 0
        return sum(col_data)/ len(col_data)

    result = []
    for i in range(0, len(cities)):
        city_data = [row for row in data[i] if row[0] is not None]
        average_value = get_average_for_city(city_data)
        result.append((cities[i], average_value))

    return result




def get_modes(col, data, cities):
    
    TOL = 0.02
    modes_list = []
    for city_index, city in enumerate(cities):
        col_vals = []
        for row in data[city_index]:
            col_vals.append(row[col])
        col_vals.sort()
        modes = []
        max_count = 0
        current_count = 1
        current_val = col_vals[0]
        for i in range(1, len(col_vals)):
            if abs(col_vals[i] - current_val) <= TOL:
                current_count += 1
            else:
                if current_count > max_count:
                    modes = [current_val]
                    max_count = current_count
                elif current_count == max_count:
                    modes.append(current_val)
                current_val = col_vals[i]
                current_count = 1
        
        if current_count > max_count:
            modes = [current_val]
            max_count = current_count 

        elif current_count == max_count: 
            modes.append(current_val)
        modes_list.append((city, modes, max_count)) 
    return modes_list 
          
def high_low_averages(data, cities, categories):
    
    category_indices = [COLUMNS.index(cat) if cat in COLUMNS else None for cat in categories]
    results = []

    for category_index in category_indices:
        category_list = []
        if category_index is None:
            results.append(None)
            continue
        
        averages = []
        for city_data in data:
            if not city_data:
                continue
            
            city_average = 0
            count = 0
            for row in city_data: 
                if row[category_index] is None:
                    continue

                city_average += row[category_index]
                count += 1

            if count == 0:
                continue

            city_average /= count
            averages.append((city_average, city_data[0][0]))

        if not averages:
            results.append(None)
            continue

        max_average, max_city = max(averages)
        min_average, min_city = min(averages)
        category_list.append((min_city, min_average))
        category_list.append((max_city, max_average))
        results.append(category_list)

    return results

'''def get_modes(col, data, cities):
    modes = []
    for city in enumerate(cities):
        cat = [info[col] for info in data[city[0]] if info[col] != \
               None and type(info[col]) != str]
        cat.sort(reverse=True)
        reps = []
        count = 1
        prev = cat[0]
        for i in range(1, len(cat)):
            diff = prev = cat[i]
            issue = abs(diff / prev)

            if issue <= TOL:
                count += 1
            else:
                reps.append((count, prev))
                count = 1
            
            prev = cat[i]

            if i == len(cat) - 1:
                reps.append((count, prev))
        
        reps.sort(reverse = True)
        counter_max = reps[0][0]
        repeats = [x[1] for x in reps if x[0] == counter_max]
        if counter_max == 1:
            repeats = []
        modes.append((city[1], sorted(repeats), counter_max))
    return modes'''



            





def display_statistics(col,data, cities):
    
    for city in cities:
        city_data = []
        for row in data:
            if row[0][0] == city:
                city_data.append(row[col][1])
        if city_data:
            maximum = get_max(city_data)
            minimum = get_min(city_data)
            average = get_average(city_data)
            modes = get_modes(city_data)
            print(city + ":")
            print("Min:", format(minimum, ".2f"), "Max:", format(maximum, ".2f"), "Avg:", format(average, ".2f"))
            if modes:
                modes_str = ', '.join(str(mode) for mode in modes)
                print("Most common repeated values ({} occurrences): {}".format(len(modes), modes_str))
            else:
                print("No modes.")
             
def main():
    print(BANNER)
    file_pointer = open_files()
    cities = file_pointer[0]
    data = read_files(file_pointer[1])

    
    while True:
        print(MENU)

        try:
            option = input()
        except EOFError:
            break 
        
        def option_1(data):
            start_date = get_valid_date("Enter start date (MM/DD/YYYY): ")
            end_date = get_valid_date("Enter end date (MM/DD/YYYY): ")
            category = input("Enter a category: ")
            if category.lower() not in map(str.lower, COLUMNS):
                print("Invalid category.")
                return
            col_idx = COLUMNS.index(category.lower())
            max_vals = {}
            for city_data in data:
                city_name = city_data[0][0]
                max_val = max(filter(lambda x: start_date <= x[0] <= end_date, city_data), key=itemgetter(col_idx))[col_idx]
                max_vals[city_name] = max_val
                print(f"Max for {city_name}: {max_val:.2f}")

        
   

        
    

    

#DO NOT CHANGE THE FOLLOWING TWO LINES OR ADD TO THEM
#ALL USER INTERACTIONS SHOULD BE IMPLEMENTED IN THE MAIN FUNCTION
if __name__ == "__main__":
    main()
                                           
