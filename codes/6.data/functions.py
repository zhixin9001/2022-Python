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


def get_reds_3area(reds):
    area1 = list(range(1, 13))
    area2 = list(range(13, 25))
    area3 = list(range(25, 36))
    dic_case = {}
    for red in reds:
        area1_count, area2_count, area3_count = 0, 0, 0
        for boll in red:
            if (boll in area1):
                area1_count += 1
            elif boll in area2:
                area2_count += 1
            elif boll in area3:
                area3_count += 1
        key = f'{area1_count}-{area2_count}-{area3_count}'
        value = dic_case.get(key, 0)
        dic_case[key] = value+1
    return dic_case


def get_reds_4area(reds):
    area1 = [1, 2, 3, 7, 8, 9, 13, 14, 15]
    area2 = [4, 5, 6, 10, 11, 12, 16, 17, 18]
    area3 = [19, 20, 21, 25, 26, 27, 31, 32, 33]
    area4 = [22, 23, 24, 28, 29, 30, 34, 35]

    dic_case = {}
    for red in reds:
        area1_count, area2_count, area3_count, area4_count = 0, 0, 0, 0
        for boll in red:
            if (boll in area1):
                area1_count += 1
            elif boll in area2:
                area2_count += 1
            elif boll in area3:
                area3_count += 1
            elif boll in area4:
                area4_count += 1
        key = f'{area1_count}-{area2_count}-{area3_count}-{area4_count}'
        value = dic_case.get(key, 0)
        dic_case[key] = value+1
    return dic_case


def get_ac_count(inputs, nums):
    ac_count = {}
    for bolls in inputs:
        diffs = set()
        for boll1 in bolls:
            for boll2 in bolls:
                diffs.add(abs(boll1-boll2))
        ac = len(diffs)-1-(nums-1)
        count = ac_count.get(ac, 0)
        ac_count[ac] = count+1
    return ac_count


def draw_plot(sums, avgs, color='red'):
    fig, ax = plt.subplots(figsize=(18, 3))
    ax.plot(sums, color=color)
    ax.plot(avgs, color='gray')
    plt.show()


def draw_bar(x, y, rotation=0):
    fig, ax = plt.subplots(figsize=(18, 3))
    ax.bar(x, y)
    plt.xticks(rotation=rotation)
    plt.show()
