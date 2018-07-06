"""
Calculating average and standard deviation
for 4 variable in "iris.data".
"""
import numpy as np
import math

#orig_lists
sepal_length_list = []
sepal_width_list = []
petal_length_list = []
petal_width_list = []

#データを読みこみ整形
with open ("iris.data") as file:
    stuck_sample_list = file.read().split("\n")

while True:
    try:
        stuck_sample_list.remove("")
    except ValueError:
        break

SAMPLE_NUM = len(stuck_sample_list)#サンプルデータの個数

for i in range(SAMPLE_NUM):
    sample_list = stuck_sample_list[i].split(",")
    sepal_length_list.append(float(sample_list[0]))
    sepal_width_list.append(float(sample_list[1]))
    petal_length_list.append(float(sample_list[2]))
    petal_width_list.append(float(sample_list[3]))


def count_variables(sample_list):#サンプルのfloatの要素数をカウント(変数をカウント)
    """
    Counting variables per one sample in the "iris.data".
    "sample_list" use a last sample data in the "iris.data".
    """
    float_variable = []

    for i in sample_list:
        try:
            float_variable.append(float(i))
        except:
            pass

    return len(float_variable)


def average(orig_lists):#平均値を求める
    """
    Calculating average for each variable in "iris.data".
    "orig_lists" is a list of each variable.
    """
    average = sum(orig_lists) / SAMPLE_NUM

    return average


def standard_deviation(orig_lists, average):#標準偏差を求める
    """
    Calculating standard deviation for each variable in "iris.data".
    "orig_lists" is a list of each variable.
    "average" is a average. [carculating by function "average()"].
    """
    num_list = []

    for i in orig_lists:
        num_list.append((i - average) ** 2)

    dispersion = sum(num_list) / SAMPLE_NUM
    standard_deviation = np.around(math.sqrt(dispersion), 2)

    return standard_deviation


cut_sepal_length = np.around(average(sepal_length_list), 2)
cut_sepal_width = np.around(average(sepal_width_list), 2)
cut_petal_length = np.around(average(petal_length_list), 2)
cut_petal_width = np.around(average(petal_width_list), 2)

print("iris.dataには",SAMPLE_NUM,"個のサンプルデータが列挙されています。")
print(count_variables(sample_list),"変数について平均値・標準偏差を求めた結果を以下に示します。")
print("sepal length: average =",cut_sepal_length,", standard deviation =",standard_deviation(sepal_length_list,average(sepal_length_list)))
print(" sepal width: average =",cut_sepal_width,", standard deviation =",standard_deviation(sepal_width_list,average(sepal_width_list)))
print("petal length: average =",cut_petal_length,", standard deviation =",standard_deviation(petal_length_list,average(petal_length_list)))
print(" petal width: average =",cut_petal_width,", standard deviation =",standard_deviation(petal_width_list,average(petal_width_list)))
