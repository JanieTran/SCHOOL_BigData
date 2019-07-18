import pandas as pd
from early_alert_numerical_analysis.problem1_populations.helpers import get_digit, generate_plot


def generate_populations_digit_plot_from_1980():
    # Skip 4 starting rows and drop rows containing NaN
    pop_df = pd.read_csv('Populations.csv', skiprows=4)
    pop_df.drop(pop_df.columns[-1], axis=1, inplace=True)
    pop_df.dropna(inplace=True)

    # Only keep rows from year 1980 to 2017
    years = list(map(str, list(range(1980, 2018))))
    pop_df = pop_df[years]

    # Get starting and ending digit for each year
    for year in years:
        pop_df[year] = get_digit(pop_df[year])

    # Initialise list to store digit frequency
    start_digit_count = [0] * 10
    end_digit_count = [0] * 10

    # Iterate through dataframe and record occurrence of digit
    for index, row in pop_df.iterrows():
        for year in years:
            start_digit_count[int(row[year][0])] += 1
            end_digit_count[int(row[year][1])] += 1

    # Generate distribution plot
    generate_plot(digit_distribution=start_digit_count, year='1980_2017', start=True)
    generate_plot(digit_distribution=end_digit_count, year='1980_2017', start=False)


if __name__ == '__main__':
    generate_populations_digit_plot_from_1980()
