'''
Problem Definition
You will have access to the following raw data files:
1. A file containing the number of employees by locations (US Census Public Use
Microdata Area PUMA) and occupations

2. A file containing the average salary for each occupation

You will need to use these files to produce one new file containing the locations and their
average salary and total salary.
Each row in this new file will contain the name of a location and
the columns will show the value of the average salary and total salary for that location. The
resulting file should be sorted by total salary descending.

We will evaluate this assignment considering the following criteria:

Considerations

Performance (will your approach scale?)
Reusability of code (is it properly organized?)

Bonus (not required)
Add a third column with the entropy of labor share for each location.
Add a fourth column with the highest paid occupation for each location.

'''
import csv
import itertools
import pandas as pd


def find_separator(csv_file):
    # find separator:
    # load the first few lines, to guess the CSV dialect
    head = ''.join(itertools.islice(open(csv_file), 5))
    s = csv.Sniffer()
    my_separator = s.sniff(head).delimiter
    return my_separator


def read_puma_file(puma_file):
    '''
    Here we read the puma file.
    '''
    print("processing PUMA file")
    # could have read remote file, but it would have been harder to find its separator.
    my_sep = find_separator(puma_file)
    df_puma_file = pd.read_csv(puma_file, sep=my_sep)
    #df_puma_file['total_salary'] = df_puma_file['total_population']*df_puma_file['average_wage']
    #df_puma_wage_per_location = df_puma_file.groupby('puma_name')['total_salary'].sum()
    print(df_puma_file.head(10).to_string())
    print(df_puma_file.size)

    return df_puma_file


def read_average_salaries_file(average_salaries_file):
    '''
    here we read the average salaries file
    :return:
    '''
    print("Processing averages file")
    my_sep = find_separator(average_salaries_file)
    df_avg_file = pd.read_csv(average_salaries_file, sep=my_sep)
    print(df_avg_file.head(10).to_string())
    print(df_avg_file.size)
    return df_avg_file


def merge_files(df_puma, df_avg):
    '''
    columns: locations, average salary, total salary.
    sorted by total salary descending.
    :return:
    '''
    # to find column names to do the merge
    print(list(df_puma))
    print(list(df_avg))
    # do the actual merge
    df_merged = pd.merge(df_puma, df_avg, left_on='occupation_id', right_on='ID Detailed Occupation', how='left')
    # locations (puma_name, perhaps I should drop PUMA)
    # and their average salary (Average Wage)
    # and total salary ('total_population' * 'average_wage')

    df_merged['total_salary'] = df_merged['total_population'] * df_merged['average_wage']

    df_merged.rename(columns={'puma_name': 'Location'},
                     inplace=True)

    # This is th actual assignment
    total_salary = df_merged.groupby('Location')['total_salary'].sum()

    average_salary = df_merged.groupby('Location')['Average Wage'].mean()

    result = pd.concat([total_salary, average_salary], axis=1)
    result.rename(columns={'total_salary': 'Total salary',
                           'Average Wage': 'Average salary'},
                  inplace=True)
    result.sort_values(by=['Total salary'], ascending=False, inplace=True)
    result.to_csv('assignment.csv')
    return result



def add_entropy():
    '''
    entropy = sum[(probability of i) times (log base 2 (probability of i)]
    :return:
    '''


def add_highest_paid_per_location(df_puma, df_avg):
    '''
    Add a fourth column with the highest paid occupation for each location.

    :return:
    '''

    df_merged = pd.merge(df_puma, df_avg, left_on='occupation_id', right_on='ID Detailed Occupation', how='left')
    # locations (puma_name, perhaps I should drop PUMA)
    # and their average salary (Average Wage)
    # and total salary ('total_population' * 'average_wage')

    df_merged['total_salary'] = df_merged['total_population'] * df_merged['average_wage']

    df_merged.rename(columns={'puma_name': 'Location'},
                     inplace=True)

    print(df_merged.head(10).to_string())
    idx = df_merged.groupby('Location')['Average Wage'].transform(max) == df_merged['Average Wage']

    print(df_merged[idx].size)


if __name__ == '__main__':
    print('Resolving the assignment')
    my_df_puma = read_puma_file('../data/pumas_occupations_num_employees.csv')
    my_df_avg = read_average_salaries_file('../data/occupations_avg_wage.csv')
    merge_files(my_df_puma, my_df_avg)
    #add_highest_paid_per_location(my_df_puma, my_df_avg)
