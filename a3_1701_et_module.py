def execute_(cmd:str, table:list) -> list:
    """ Executes commands entered by the user """

    instruction_list = cmd.split(" ")
    command = instruction_list[0]
    other_instructions = instruction_list[1:]
    
    if command == "count":
        print(count(table))
        
    elif command == "columns":
        print_table(columns(table))

    elif command == "distr":
        table = distr(other_instructions, table)
        print(count(table))

    elif command == "print":
        print_table(table)
        print(count(table))

    elif command == "project":
        table = project(other_instructions, table)
        print(count(table))

    elif command == "read":
        table = read(other_instructions)
        print(count(table))

    elif command == "select":
        table = select(other_instructions, table)
        print(count(table))

    elif command == "sort":
        table = sort(other_instructions, table)
        print(count(table))

    elif command == "save":
        save(table, other_instructions)

    else:
        print(f"{command}: Command not recognized")

    return table


def read(instruction_list:list) -> list:
    """ Reads the CSV file and loads it to the current table """

    filename = instruction_list[0]
    file = open(filename, "r")
    line = file.readline()
    line = line.strip().split(",")

    table = []

    while line != [""]:

        table.append(line)
        line = file.readline()
        line = line.strip().split(",")

    file.close()

    return table


def print_table(table:list) -> None:
    """ Prints the current table """

    header = ""

    for column in table[0]:
        header += f"{column}\t  "
    
    separator = "-" * len(header)

    print(separator)
    print(header)
    print(separator)

    for row in table[1:]:
        row_string = ""

        for item in row:
            if len(item) >= 9:
                row_string += f"{item} "
            else:
                row_string += f"{item}\t "

        print(row_string)

    print(separator)


def count(any_list:list) -> str:
    """ Prints the number of rows for any table """

    rows = f"{len(any_list) - 1} rows"

    return rows
    

def columns(any_list:list) -> list:
    """ Prints the column names for the current table """

    columns_list = [["Columns"]]

    for item in any_list[0]:
        columns_list.append([item])
    
    return columns_list


def select(instructions:str, table:list) -> list:
    """ Creates a new current table with the rows selected """

    new_table = []
    new_table.append(table[0])
    value = instructions[1]

    for lst in table[1:]:
        if value in lst:
            new_table.append(lst)

    return new_table


def project(columns_list:list, table:list) -> list:
    """ Creates a new current table with the columns listed"""

    new_table = []
    new_table.append(columns_list)
    temp_list = []

    counter = 1
    length = len(table)

    while counter < length:
        for column in columns_list:

            idx = table[0].index(column)
            temp_list.append(table[counter][idx])

        new_table.append(temp_list)
        temp_list = []
        counter += 1

    return new_table


def sort(column:list, table:list) -> list:
    """ Creates a new current table, sorted in ascending 
    order of the values in the column selected"""
    ### [1] 
    
    column_selected = column[0]
    header = table.pop(0)
    idx = header.index(column_selected)
    length = len(table)

    for i in range(length):

        min_index = i
        min_value = table[i][idx]

        for j in range(i + 1, length):

            next_value = table[j][idx]

            if next_value < min_value:
                min_index = j
                min_value = next_value

        swap(table, i, min_index)
    
    table.insert(0, header)

    return table


def swap(any_list:list, i:int, j:int) -> list:
    """ Swaps the smallest value found by sort function with the value at index i """

    temp = any_list[i]
    any_list[i] = any_list[j]
    any_list[j] = temp

    return any_list


def distr(column:list, table:list) -> list:
    """ Creates a new table with the value from column and 
    a count of the number of rows containing the column value """

    column_selected = column[0]
    idx = table[0].index(column_selected)
    new_table = []
    new_table.append([column_selected, "Count"])

    i = 1

    while i < len(table):

        value = table[i][idx]
        count = 0
        value_in_list = False
        
        for lst in new_table:
            if value in lst:
                value_in_list = True

        if value_in_list == False:
                        
            for lst in table[1:]:
                if value in lst: 
                    count += 1

            new_table.append([value, str(count)])

        i += 1

    return new_table


def save(table:list, instruction_list:list) -> None:
    """ Saves the current table to a csv file """

    filename = instruction_list[0]
    savefile = open(filename, "w")

    for line in table:
        write_string = ""
        glue = ","
        write_string = glue.join(line)
        write_string += ("\n")

        savefile.write(write_string)

    savefile.close()