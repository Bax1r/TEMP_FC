"""
File Name: Simple.py
Author: Bryan Insfran
Description: Class meant to simplify the use
of sqlite3 by creating methods for that run
the sqlite commands in a neater manner

Warning: Must pass all parameters as strings
Example: self.insert('table_name', 'values')
"""

class Simplify():
    def __init__(self):
        pass

    # Creates a table with the given name
    # Can take any number of varible arguments
    def create_table(self, name, *vars):
        initial = ('''CREATE TABLE ''' + name + ''' (''')
        
        temp = 0

        for var in vars:
            if temp == 0:
                initial += var
                temp += 1
                continue
            initial += (''', ''')
            initial += var

        initial += ''');'''

        return initial

    # Deletes given table if it already exists
    def remove_table(self, table):
        return('''DROP TABLE IF EXISTS ''' + table)

    # Similar to create_table inserts into given table
    # Can take any number of values (should be the amount of "columns" in a table)
    def insert(self, table, *values):
        formatted_values = []

        for value in values:
            if isinstance(value, str):
                formatted_values.append(f"'{value}'")  # Wrap strings in single quotes
            else:
                formatted_values.append(str(value))  # Convert non-strings to strings

        values_str = ", ".join(formatted_values)

        return ('''INSERT INTO ''' + table + ''' VALUES (''' + values_str + ''')''')

    # Returns all values in given table if no condition is given, condition is optional
    # Condition arugment runs on comparison operators (=, >=, <=, !=, LIKE, NOT, etc.)
    def searchall_or_con(self, table, condition=None, condition_var=None, *vars):
        if condition == None and vars == None:
            return ('''SELECT * FROM ''' + table)
        elif vars == None:
            return ('''SELECT * FROM ''' + table + ''' WHERE ''' + condition + condition_var)
        else:
            return (self.search_vars(table, vars) + '''WHERE''' + condition + condition_var)

    def search_vars(self, table, *vars):
        initial = '''SELECT '''
        
        temp = 0

        for var in vars:
            if temp == 0:
                initial += var
                temp += 1
                continue
            initial += (''',''')
            initial += var

        initial += ''' FROM '''
        initial += table

        return initial
    
    # Ordered by ASC or DESC
    # Order_var correspondes to a column
    def ordered_search(self, table, order_var, order='ASC', *vars):
        found = self.search_vars(table, *vars)
        
        found += ''' ORDER BY '''
        found += (order_var + ''' ''')
        found += order

        return found

    # Deletes any entry that matches given condition
    def remove(self, table, condition=None):
        if condition == None:
            return ('''DELETE from ''' + table)
        return ('''DELETE from ''' + table + ''' WHERE ''' + condition)
    
    def update_vars(self, table, condition=None, *vars):
        temp = 0

        for var in vars:
            if temp == 0:
                vari = var
                temp += 1
                continue
            vari += (''', ''')
            vari += var

        if condition == None:
            return ('''UPDATE ''' + table + ''' SET ''' + vari)
        return ('''UPDATE ''' + table + ''' SET ''' + vari + ''' WHERE ''' + condition)