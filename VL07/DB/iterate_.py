"""Join cells together in pandas format"""

import pandas as pd
# ["_".join([my_variable, i]) for i in my_list]

def excel_reader(file):
    """Join a file in pandas"""
    file = pd.read_excel(file, header=None, sheet_name="Sheet1")
    file[3] = file[0] + ' ' + file[1]
    output = file.to_excel("D:/output_file2.xlsx", index=False, header=False)
    return output

myfile = "D:/IS360_Db07.xlsx"
excel_reader(myfile)
