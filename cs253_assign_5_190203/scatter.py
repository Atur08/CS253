import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pwd = os.path.dirname(__file__)
sk = pd.read_csv(open(os.path.join(pwd, 'Data/new_skdata.csv'), "r"))
srk = pd.read_csv(open(os.path.join(pwd, 'Data/new_srkdata.csv'), "r"))
ak = pd.read_csv(open(os.path.join(pwd, 'Data/new_akdata.csv'), "r"))

def rating(y):
    # Function that maps the verdicts to the corresponding numbers and 
    # then returns the array 

    # All Time Blockbuster = 10
    # Blockbuster = 9
    # Super-Hit = 8
    # Hit = 7
    # Semi-Hit = 6
    # Average = 5
    # Flop = 4
    new_rating = np.empty(0)
    for x in y:
        if(x == "All Time Blockbuster"):
            new_rating = np.append(new_rating, 10)
        if(x == "Blockbuster"):
            new_rating = np.append(new_rating, 9)
        if(x == "Super-Hit"):
            new_rating = np.append(new_rating, 8)
        if(x == "Hit"):
            new_rating = np.append(new_rating, 7)
        if(x == "Semi-Hit"):
            new_rating = np.append(new_rating, 6)
        if(x == "Average"):
            new_rating = np.append(new_rating, 5)
        if(x == "Flop"):
            new_rating = np.append(new_rating, 4)
    return new_rating


def modify(y):
    new = y[y['Lifetime'] != "N.A"]
    new.Lifetime = new.Lifetime.astype(float)
    return new


#modify the data sets
sk_new = modify(sk)
srk_new = modify(srk)
ak_new = modify(ak)


sk_new_rating = rating(sk_new.Verdict)
srk_new_rating = rating(srk_new.Verdict)
ak_new_rating = rating(ak_new.Verdict)


plt.scatter(sk_new_rating, sk_new.Lifetime)
plt.scatter(srk_new_rating, srk_new.Lifetime, marker='^')
plt.scatter(ak_new_rating, ak_new.Lifetime, marker='s')

plt.xlabel("Verdict", fontweight="bold")
plt.ylabel("Box Office Collection in rupees(Cr)", fontweight="bold")
plt.title("Interrelation between earnings and final verdicts", fontweight="bold")

plt.legend(['SK', 'SRK', 'AK'])
#plt.show()
plt.savefig(os.path.join(pwd, 'Plots/scatter.png'), dpi=200)
plt.close()
