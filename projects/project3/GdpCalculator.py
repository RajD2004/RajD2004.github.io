

def open_file():
    
    '''Prompts user for a file input. Keeps reprompting for file input until a valid file that is openable is inputted'''

    file_name = input("Enter file name: ")
    done = False
    while not done:
        try:
            file_pointer = open(file_name, 'r')
            done = True
            break
        except FileNotFoundError:
            print("INVALID FILE")
            file_name = input("Enter file name: ")
    return file_pointer 

def find_index(line, value):
    
    '''Does the opposite of find_gdp(). Finds the index of a value in a line in the file'''

    empt_str = ''
    index_val = 0
    for char in line:
        if char.isdigit() == True or char == "." or char == "-":
            empt_str += char
        elif char == " ":
            if empt_str:
                empt_flt = float(empt_str)
                if empt_flt == value:
                    return index_val
                    break
                empt_str = ''
                index_val += 1 

def find_min_value(line):
    
    '''finds min value by iterating through and comparing each number with each other'''

    empt_str = ''
    min_value = 9999999.9

    for char in line:
        if char != " ":
            empt_str += char
        else:
            if empt_str:
                empt_str = float(empt_str)
                if empt_str < min_value:
                    min_value = empt_str
                empt_str = ''
    year_min = find_index(line, min_value) + 1969
    
    return year_min, min_value

                                             
def find_max_value(line):
    
    '''Finds max value by iterating through and comparing all the values in the file '''
    
    empt_str = ''
    max_value = 1.0
    for char in line:
        if char != " ":
            empt_str += char 
        else:
            i = 0
            while i < 6:
                i += 1
                continue
            if i == 6:
                try:
                    empt_str = float(empt_str)
                    if max_value < empt_str:
                        max_value = empt_str
                    empt_str = ''
                    
                except ValueError:
                    continue
                    
                continue
    
    year_max = find_index(line, max_value) + 1969
    return year_max, max_value

def find_gdp(line, index_value):
    
    '''finds the value in a line of the file given an index value'''

    line += "      "
    empt_str = ''
    index_val = 0
    for char in line:
        if char != " ":
            empt_str += char
        else:
            if empt_str:
                empt_flt = float(empt_str)
                if index_val == index_value:
                    return empt_flt
                    break
                index_val += 1
                empt_str = ''

def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    
    '''Displays outputs of all the functions'''

    HEADER = '\nGross Domestic Product'
    print(HEADER)
    print("{:<10s}{:>8s}{:>6s}{:>18s}".format("min/max","change","Year","GDP (trillions)"))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("min",min_val,min_year,min_val_gdp))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("max",max_val,max_year,max_val_gdp))

def main():
    
    new_line = 1
    file_pointer = open_file()
    for line in file_pointer:
        for char in line:
            if char != '\n':
                continue
            else:
                new_line += 1
                if new_line == 10:
                    line_seg = line[76:len(line) + 1]
                    index_val_min, minimum_val = find_min_value(line_seg)
                    index_val_max, maximum_val = find_max_value(line_seg)
                elif new_line == 45:
                    line_seg2 = line[80:len(line) + 1]
                    min_val_gdp = round(find_gdp(line_seg2, index_val_min-1969) / 1000, 2)
                    max_val_gdp = round(find_gdp(line_seg2, index_val_max-1969) / 1000, 2)
    
        
    display(minimum_val, index_val_min, min_val_gdp, maximum_val, index_val_max, max_val_gdp)

if __name__ == "__main__":
    main()