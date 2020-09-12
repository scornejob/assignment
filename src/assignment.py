'''
Problem Definition
You will have access to the following raw data files:
1. A file containing the number of employees by locations (US Census Public Use
Microdata Area PUMA) and occupations
2. A file containing the average salary for each occupation
You will need to use these files to produce one new file containing the locations and their
average salary and total salary. Each row in this new file will contain the name of a location and
the columns will show the value of the average salary and total salary for that location. The
resulting file should be sorted by total salary descending.
We will evaluate this assignment considering the following criteria:
Considerations
● Performance (will your approach scale?)
● Reusability of code (is it properly organized?)
Bonus (not required)
● Add a third column with the entropy of labor share for each location.
● Add a fourth column with the highest paid occupation for each location.

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
    my_sep = find_separator(puma_file)
    df_puma_file = pd.read_csv(puma_file, sep=my_sep)



def read_average_salaries_file(average_salaries_file):
    '''
    here we read the average salaries file
    :return:
    '''

def merge_files():
    '''
    columns: locations, average salary, total salary.
    sorted by total salary descending.
    :return:
    '''


def add_entropy():
    '''
    entropy = sum[(probability of i) times (log base 2 (probability of i)]

    :return:
    '''


def add_highest_paid_per_location():



if __name__ == '__main__':
    print('Resolving the assignment')