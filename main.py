import pandas as pd
import numpy as np
import statistics as st
import seaborn as sns
from scipy.stats import gmean
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde



def Introduction():
    print("Klymenko Maksym TK-32 Lab1")
    print("Heart Attack Analysis")
def PrintVariables(data):
    print('List of column names: ', list(data.columns))
    print("I'm going to analyse 3 scalar variables: age(Age of the person), "
          "trtbps(resting blood pressure (in mm Hg)) "
          "and thalachh(maximum heart rate achieved)")
    print("Amount of data: " + str(len(data)))
def Plotbuilder(data, y = 60):
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
    plt.show()
    sns.swarmplot(data, color="black") #stripplot рисует диаграмму рассеяния
    sns.violinplot(data, color="orange")
    plt.show()



Introduction()
print("")

data = pd.read_csv('heart.csv')
PrintVariables(data)
#n = (input("Press anything to view plots"))

Plotbuilder(data['age'], 70)
Plotbuilder(data['trtbps'])
Plotbuilder(data['thalachh'])











