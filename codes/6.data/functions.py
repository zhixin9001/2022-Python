import csv
import matplotlib.pyplot as plt
import math


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


def get_diff_count(diffs, step=10):
    max_value = (max(diffs))
    x_nums = math.ceil(max_value/step)
    diff_count = {}
    for index in range(0, x_nums):
        diff_count[f'{index*step}-{(index+1)*step}'] = 0

    for index in range(0, x_nums):
        start = index*step
        end = (index+1)*step
        diff_count[f'{start}-{end}'] = (len(list(filter(lambda x: x >=
                                                        start and x < end, diffs))))
    return diff_count
