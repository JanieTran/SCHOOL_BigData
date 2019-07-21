import pandas as pd


def get_sequence(n):
    steps = 0
    max_number = 0

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
        max_number = max(n, max_number)

    return steps, max_number


if __name__ == '__main__':
    stats_df = pd.DataFrame(columns=['steps', 'max'], index=range(1, 101))

    same_number_step = []

    for i in range(1, 101):
        steps, max_number = get_sequence(i)
        if steps == i:
            same_number_step.append(i)
        stats_df.loc[i, 'steps'] = steps
        stats_df.loc[i, 'max'] = max_number

    max_step = stats_df['steps'].max()
    max_number_overall = stats_df['max'].max()

    print(stats_df)
    print('Overall max number reached:', max_number_overall)
    print('Numbers taking most steps:', stats_df[stats_df['steps'] == max_step].index.tolist())
    print('Numbers take exactly the same number of steps to reach 1 as itself:', same_number_step)
