import csv
import matplotlib.pyplot as plt


def get_data(csv_path):
    with open(csv_path) as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        counter = 1
        reds, blues, red_blues = [], [], []
        while counter <= 800:
            row = next(csv_reader)
            splited = row[2].split()
            red_blues.append(list(map(int, splited)))
            reds.append(list(map(int, splited[:-2])))
            blues.append(list(map(int, splited[-2:])))
            counter += 1
    return (reds, blues, red_blues)


def get_sum_avg_diff(source, avg_total):
    sums = list(map(sum, source))
    avgs = list(map(lambda _: avg_total, source))
    diffs = list(map(lambda x: abs(x-avg_total), sums))
    return (sums, avgs, diffs)


def draw_plot(sums, avgs, color='red'):
    fig, ax = plt.subplots(figsize=(18, 3))
    ax.plot(sums, color=color)
    ax.plot(avgs, color='gray')
    plt.show()


def draw_bar(x, y):
    fig, ax = plt.subplots(figsize=(18, 3))
    ax.bar(x, y)
    plt.show()


def get_diff_count(diffs):
    diff_count = {'0-10': 0, '10-20': 0, '20-30': 0,
                  '30-40': 0, '40-50': 0, '50-60': 0}
    diff_count['0-10'] = (len(list(filter(lambda x: x >=
                          0 and x < 10, diffs))))
    diff_count['10-20'] = (len(list(filter(lambda x: x >=
                           10 and x < 20, diffs))))
    diff_count['20-30'] = (len(list(filter(lambda x: x >=
                                           20 and x < 30, diffs))))
    diff_count['30-40'] = (len(list(filter(lambda x: x >=
                                           30 and x < 40, diffs))))
    diff_count['40-50'] = (len(list(filter(lambda x: x >=
                                           40 and x < 50, diffs))))
    diff_count['50-60'] = (len(list(filter(lambda x: x >= 50, diffs))))
    return diff_count
