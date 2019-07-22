import pandas as pd
import matplotlib.pyplot as plt


def golden_ratio_population(year):
    # Read from CSV and only take record of the desired year
    pop_df = pd.read_csv('Populations.csv', skiprows=4, usecols=[year]).dropna()
    # Sort values from largest to smallest
    pop_df.sort_values(by=year, axis=0, ascending=False, inplace=True)
    # Reset index to avoid errors when indexing later
    pop_df.reset_index(drop=True, inplace=True)
    # Initalise column to store estimated value
    pop_df.loc[0, 'estimated'] = pop_df.loc[0, year]

    # Iterate through dataframe top down, next value is estimated by
    # taking the previous value and dividing it by the golden ratio
    for i in range(1, pop_df.shape[0]):
        pop_df.loc[i, 'estimated'] = pop_df.loc[i - 1, year] / 1.61803398875

    # Generate plot to present results
    fig, ax = plt.subplots()
    ax.plot(pop_df[year], label='Actual', linewidth=5)
    ax.plot(pop_df['estimated'], label='Actual', linewidth=2)
    plt.title('Actual vs estimated population in year {}'.format(year))
    plt.ylabel('Population')
    plt.legend(['Actual', 'Estimated'])
    plt.savefig('golden_ratio_population_{}.png'.format(year))


def golden_ratio_fibonacci(n):
    fibonacci = pd.DataFrame(columns=['actual', 'estimated'], index=range(n))
    fibonacci.loc[0:2, 'actual'] = 1

    for i in range(2, n):
        fibonacci.loc[i, 'actual'] = fibonacci.loc[i - 1, 'actual'] + fibonacci.loc[i - 2, 'actual']

    fibonacci.sort_values(by='actual', axis=0, ascending=False, inplace=True)
    fibonacci.reset_index(drop=True, inplace=True)
    fibonacci.loc[0, 'estimated'] = fibonacci.loc[0, 'actual']

    for i in range(1, fibonacci.shape[0]):
        fibonacci.loc[i, 'estimated'] = fibonacci.loc[i - 1, 'actual'] / 1.61803398875

    # Generate plot to present results
    fig, ax = plt.subplots()
    ax.plot(fibonacci['actual'], label='Actual', linewidth=5)
    ax.plot(fibonacci['estimated'], label='Actual', linewidth=2)
    plt.title('Actual vs estimated {} numbers in Fibonacci sequence'.format(n))
    plt.ylabel('Number')
    plt.legend(['Actual', 'Estimated'])
    plt.savefig('golden_ratio_fibonacci_{}.png'.format(n))


if __name__ == '__main__':
    golden_ratio_population('1998')
    golden_ratio_fibonacci(50)
