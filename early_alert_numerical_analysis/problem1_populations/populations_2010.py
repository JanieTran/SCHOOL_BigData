import pandas as pd
from early_alert_numerical_analysis.problem1_populations.helpers import get_digit, generate_plot


def generate_population_digit_plots():
    # Skip 4 starting rows and only load Country Code and 2010 columns, finally drop rows containing NaN
    pop_df = pd.read_csv('Populations.csv', skiprows=4, usecols=['Country Code', '2010']).dropna()

    # Get starting and ending digit
    pop_df['2010'] = get_digit(pop_df['2010'])

    # Initialise list to store digit frequency
    start_digit_count = [0] * 10
    end_digit_count = [0] * 10

    # Iterate through dataframe and record occurrence of digit
    for index, row in pop_df.iterrows():
        start_digit_count[int(row['2010'][0])] += 1
        end_digit_count[int(row['2010'][1])] += 1

    # Generate plot for starting digit
    generate_plot(digit_distribution=start_digit_count, year='2010', start=True)
    # Generate plot for ending digit
    generate_plot(digit_distribution=end_digit_count, year='2010', start=False)


if __name__ == '__main__':
    generate_population_digit_plots()
