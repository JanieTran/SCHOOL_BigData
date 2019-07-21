import matplotlib.pyplot as plt


# Number of Fibonacci numbers
n_numbers = 150000

# Initialise fibonacci array and digit arrays
# fibonacci = [1] * n_numbers
starting_digits = [0] * 10
ending_digits = [0] * 10
a = 0
b = 1

for i in range(n_numbers):
    # The first number is 1
    if i == 0:
        starting_digits[1] += 1
        ending_digits[1] += 1
        continue

    # Calculate the next number
    number = a + b
    a = b
    b = number

    # Record digit occurence
    number = str(number)
    starting_digits[int(number[0])] += 1
    ending_digits[int(number[-1])] += 1

    # Logging
    if i % 10000 == 0:
        print(i, end=' ')

# Generate plot for starting digit distribution
plt.title('Starting Digit Distribution in Fibonacci Sequence of {} numbers'.format(n_numbers))
plt.xlabel("Digits")
plt.ylabel("Frequency")
plt.scatter(x=list(range(10)), y=starting_digits, s=10)
plt.savefig('fibonacci_{}_start.png'.format(n_numbers))
plt.close()

# Generate plot for ending digit distribution
plt.title('Ending Digit Distribution in Fibonacci Sequence of {} numbers'.format(n_numbers))
plt.xlabel("Digits")
plt.ylabel("Frequency")
plt.scatter(x=list(range(10)), y=ending_digits, s=10)
plt.savefig('fibonacci_{}_end.png'.format(n_numbers))
plt.close()
