"""

For the code below, the following assumptions are made:
1: Each csv file imported into Pandas has the same number of column headers
2: CSV are merged by row

Non- Native Python Libraries used: Python Data Analysis Library

pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and
data analysis tools for the Python programming language. 

os library was also imported to make to make the tool OS agnostic
glob library was included to find path names with a specified pattern Unix style


"""
import os
import pandas as pd
import glob

# Path to folder than contains csv files, specifies that only csv files should be considered
path = r'C:\Users\Moyo\Downloads\Data'
all_files = glob.glob(os.path.join(path, "*.csv"))


# Imports and creates a pandas data frame for each file
df_from_each_file = (pd.read_csv(f) for f in all_files)

# Concatenates data frames that have been read in
concatenated_df = pd.concat(df_from_each_file, ignore_index=True, verify_integrity=False)


# Removes duplicates from concatenated csv file and outputs it as a tab delimited csv for clarity
df_without_duplicates = concatenated_df.drop_duplicates()
df_without_duplicates.to_csv('C:\\Users\\Moyo\\Downloads\\Data\\merged.csv', sep='\t')


# Finds rows with duplicated data and outputs both occurrences with indices specified to a tab delimited csv file
duplicated_values = concatenated_df[concatenated_df.duplicated(['playerID', 'yearID', 'stint', 'teamID', 'lgID', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'IBB', 'HBP', 'SH', 'SF', 'GIDP'], keep=False)]
duplicated_values.to_csv('C:\\Users\\Moyo\\Downloads\\Conflict\\conflict.csv', sep='\t')


