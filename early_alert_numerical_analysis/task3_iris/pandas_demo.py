"""
This program demonstrates how pandas library is used to read a csv file.

Libraries used:

sys - module which provides fucntions to interact with the interpreter.
pandas - package for easy data manipulation and analysis.

Functions used:

pandas.read_csv() - function to read all the contents of the csv file
sys.argv - array of command line arguments passed (In this program, 1)
sys.argv[1] - first command line argument passed (In this program, the file name)

To run the program:

python3 pandas_demo.py iris.csv

"""
import sys

# import the pandas library after installing it and set an allias (eg. pd)
import pandas as pd


def read_csv_file():
    """
    Function to check if there is a command line argument as the filename and
    read the CSV file using pandas library.
    :return: None
    """
    if len(sys.argv) == 1:
        print("No data file entered")
        exit(0)

    # Reading the csv file content
    df = pd.read_csv(sys.argv[1], delimiter=',')
    print("File contents: \n", df)

    # Accessing a column of the csv file
    sepal_length = df['Sepal length']
    print("Sepal length attribute contents: \n", sepal_length)

    # Printing out headers contained in the csv file
    headers = list(df)
    print("Headers: \n", headers)

    # Extracting m to n rows from the csv file, df[m:n].
    top_3 = df[0:3]
    print("Top 3 rows in the dataset: \n", top_3)

    # Filter data based on species type
    iris_setosa = df[df['Species'] == 'Iris-setosa']
    print("Data filtered based on Species type")
    print(iris_setosa)

    # Filter data based on Sepal length > 7.0
    filtered_data = df[df['Sepal length'] > 7.0]
    print("Data filtered based on one conditions")
    print(filtered_data)

    # Filter data based on two conditions
    filtered_data = df[(df['Species'].notnull()) & (df['Sepal length'] > 7.0)]
    print("Data filtered based on two conditions")
    print(filtered_data)


def main():
    """
    Main function to call the function to read a csv file
    :return: None
    """
    read_csv_file()


if __name__ == "__main__":
    main()
