import pandas as pd
import numpy as np
import statistics as st
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt



def Introduction():
    print("Klymenko Maksym TK-32 Lab1")
    print("Heart Attack Analysis")
def PrintVariables(data):
    print('List of column names: ', list(data.columns))
    print("I'm going to analyse 3 scalar variables: age(Age of the person), "
          "trtbps(resting blood pressure (in mm Hg)) "
          "and thalachh(maximum heart rate achieved)")
    print("Amount of data: " + str(len(data)))
def Plotbuilder(data, y = 70):
    sns.histplot(data, color="orange") #полігон частот
    plt.ylabel("Amount of cases")
    plt.title("Polygon of freq " + str(data.name))
    plt.ylim(0, y)
    plt.xlabel(data.name)
    plt.show()

    sns.ecdfplot(data, color="orange") #емпірична ф-ція
    plt.title("Empirical distribution function " + str(data.name))
    plt.show()

    sns.boxplot(data, color="orange") #скринька з вусами
    plt.title("Box-and-whisker plot for " + str(data.name))
    plt.show()

    sns.swarmplot(data, color="black") #stripplot рисует диаграмму рассеяния
    sns.violinplot(data, color="orange")
    plt.title("Dot plot for " + str(data.name))
    plt.show()

def Work(data):
    Introduction()
    print("")
    PrintVariables(data)
    n = (input("Press anything to continue"))
    print("")

def PrintVals(data: pd.Series):
    print(data.name)
    print("Min val: " + str(data.min()))
    print("Max val: " + str(data.max()))
    print("Median val: " + str(data.median()))
    print("First quantile(0.25): " + str(data.quantile(0.25)))
    print("Third quantile(0.75): " + str(data.quantile(0.75)))
    print("Deciles: " + str(np.quantile(data, np.arange(0, 1, 0.1))))

def CenterPosVals(data: pd.Series):
    print("Math expectation: " + str(st.mean(data)))
    print("Geometric mean: " + str(st.geometric_mean(data)))
    print("Harmonic mean: " + str(st.harmonic_mean(data)))
    print("Mode: " + str(st.mode(data)))

def ScatteringVals(data: pd.Series):
    print("Variance: " + str(st.variance(data))) #дисперсія
    print("Standard deviation: " + str(st.stdev(data))) #стандартне відхилення
    print("Variation coefficient: " + str(st.stdev(data) / st.mean(data) * 100) + "%") #коеф варіації
    print("Probable deviation: " + str((data.quantile(0.75) - data.quantile(0.25) / 2))) #ймовірнісне відхилення
    print("Sample scope: " + str(data.max() - data.min())) #розмах вибірки
    print("Concentration interval: (" + str(st.mean(data) - 3 * st.stdev(data)) #інтервал концентрації розподілу
          + ", " + str(st.mean(data) + 3 * st.stdev(data)) + ")")

def SkewnessnSharpEdging(data: pd.Series): #скошеність та гостроверхість та нормальність
    skewness = data.skew()
    print("Skewness coefficient: " + str(skewness))
    if skewness > 0:
        print("Slanted to the left.")
    elif skewness < 0:
        print("Slanted to the right.")
    else:
        print("Symmetrical.")

    kurt = data.kurt()
    print("Kurtosis coefficient: " + str(kurt))
    if kurt > 0:
        print("More pointed than normal")
    elif kurt < 0:
        print("Less pointed than normal")
    else:
        print("Just like normal")
    stat, p = stats.normaltest(data)  # Критерий согласия Пирсона
    print("P-value: " + str(p))
    if(p > 0.05):
        print("Vars are normal distributed")
    else:
        print("Vars are not normal distributed")



data = pd.read_csv('heart.csv')
vars = ['age', 'trtbps', 'thalachh']
Work(data)
for v in vars:
        PrintVals(data[v])
        print("")
        CenterPosVals(data[v])
        print("")
        ScatteringVals(data[v])
        print("")
        SkewnessnSharpEdging(data[v])
        print("")
        Plotbuilder(data[v])
        print("")
        print("")














