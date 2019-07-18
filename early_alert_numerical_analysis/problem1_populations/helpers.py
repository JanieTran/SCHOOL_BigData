import matplotlib.pyplot as plt


def get_digit(year_population):
    # Remove decimal point
    digits = year_population.apply(lambda x: str(int(x)))
    digits = digits.apply(lambda x: x[0] + x[-1])

    return digits


def generate_plot(digit_distribution, year, start):
    if start:
        digit_type = 'Starting'
    else:
        digit_type = 'Ending'

    plt.title("{} Digit Distribution in {}".format(digit_type, year))
    plt.xlabel("Digits")
    plt.ylabel("Frequency")
    plt.scatter(x=list(range(10)), y=digit_distribution, s=10)
    plt.savefig('population_{}_{}.png'.format(year, digit_type))
    plt.close()
