'''
exercise 1

def new_list_function(initial_list):
    final_list = 3 * initial_list 
    return final_list 

def main():
    initial_value = input("Enter value to be added to list: ")
    initial_list = []
    while initial_value != 'exit':
        initial_list.append(initial_value)
        initial_value = input("Enter value to be added to list: ")

    final_list = new_list_function(initial_list)
    for element in final_list:
        print(element)

main()
'''

'''
exercise 2

def return_list(in_str):
    if "," in in_str:
        in_list = in_str.split(",")
    elif " " in in_str:
        in_list = in_str.split()
    
    return in_list

in_str = 'Pranshu,Enbody,Alireza'
print(return_list(in_str))
'''

'''
exercise 3


def mutate_list(in_list, index_num, position_value):
    in_list[index_num] = position_value
    return in_list

def remove_index(in_list, index_n):
    index_num = 0
    new_list = []
    for num in in_list:
        if index_num != index_n:
            new_list.append(num)
            index_num += 1
        else:
            index_num += 1
    statement_1 = "Total elements in list = " + str(len(in_list)) 
    statement_2 = 'Total elements in list = ' + str(len(new_list))
    return new_list, statement_1, statement_2

def reverse_list(in_list):
    if in_list:
        reverse_list = in_list[::-1]
    return reverse_list
'''

'''
exercise 4

def convert_list_int(in_list):
    out_list = []
    statement = 'Error. Please enter only integers.'
    for num in in_list:
        try:
            num = int(num)
            out_list.append(num)
        except ValueError:
            return statement 
    out_tuple = tuple(out_list)
    return out_tuple
'''



        