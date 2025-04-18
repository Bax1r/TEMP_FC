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
    def search_all(self, table, condition=None):
        if condition == None:
            return ('''SELECT * FROM ''' + table)
        return ('''SELECT * FROM ''' + table + ''' WHERE ''' + condition)

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
    
    def multiples(self, table, col):
        return (f"SELECT {col}, COUNT(*) FROM {table} GROUP BY {col}")
        #return ('''SELECT ''' + col + ''',COUNT(*) FROM TABLE ''' + table + ''' GROUP BY ''' + col)

    # lists: a list containing two lists, entries and quantities: two lists of the same size, 
    # label: an entry for the first list in lists
    def yesCheck(self, lists, entries, quantities, label):
        # Takes two lists, one with labels (entries) and one with yes/no answers (quantities), 
        # and filters out the "no" answers into a new two-list pair "lists".

        if 'Yes' in entries:
            index = entries.index('Yes')
            lists[0].append(label)
            lists[1].append(quantities[index])