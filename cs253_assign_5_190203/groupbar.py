import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pwd = os.path.dirname(__file__)
sk = pd.read_csv(open(os.path.join(pwd, 'Data/new_skdata.csv'), "r"))
srk = pd.read_csv(open(os.path.join(pwd, 'Data/new_srkdata.csv'), "r"))
ak = pd.read_csv(open(os.path.join(pwd, 'Data/new_akdata.csv'), "r"))


def count_rating(y):
    # Function returns the array containing the count of each 
    #verdict 

    new_rating = np.zeros(7)
    new_rating[0] = len(y[y.Verdict == "Flop"])
    new_rating[1] = len(y[y.Verdict == "Average"])
    new_rating[2] = len(y[y.Verdict == "Semi-Hit"])
    new_rating[3] = len(y[y.Verdict == "Hit"])
    new_rating[4] = len(y[y.Verdict == "Super-Hit"])
    new_rating[5] = len(y[y.Verdict == "Blockbuster"])
    new_rating[6] = len(y[y.Verdict == "All Time Blockbuster"])

    return new_rating


sk_ratings = count_rating(sk)
srk_ratings = count_rating(srk)
ak_ratings = count_rating(ak)

""" print(sk_ratings)
print(len(sk[sk.Verdict == "Flop"]))
print(srk_ratings)
print(ak_ratings) """

points = np.arange(4, 11)

y1 = sk_ratings
y2 = srk_ratings
y3 = ak_ratings
width = 0.2

plt.bar(points-0.2, y1, width, color='blue')
plt.bar(points, y2, width, color='orange')
plt.bar(points+0.2, y3, width, color='green')

plt.xlabel("Verdict", fontweight="bold")
plt.ylabel("No. of Movies", fontweight="bold")
plt.title("Verdicts of movies of 3 Khans for the last 30 years",
          fontweight="bold")
plt.legend(["SK", "SRK", "AK"])
#plt.show()
plt.savefig(os.path.join(pwd, 'Plots/groupbar.png'), dpi=200)
plt.close()

