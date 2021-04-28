import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pwd = os.path.dirname(__file__)
sk = pd.read_csv(open(os.path.join(pwd, 'Data/new_skdata.csv'), "r"))
srk = pd.read_csv(open(os.path.join(pwd, 'Data/new_srkdata.csv'), "r"))
ak = pd.read_csv(open(os.path.join(pwd, 'Data/new_akdata.csv'), "r"))

# function to change the type of WO, WE, EOW1, LT to float from string
# and also remove those rows which do not contain the info about the 
# repective earnings (i.e. contain "N.A")
def modify(y):
    new = y.loc[(y['Opening Day'] != "N.A") & (
        y['Opening Weekend'] != "N.A") & (y['End of Week 1'] != "N.A") & (y['Lifetime'] != "N.A")]
    new['Opening Day'] = new['Opening Day'].astype(float)
    new['Opening Weekend'] = new['Opening Weekend'].astype(float)
    new['End of Week 1'] = new['End of Week 1'].astype(float)
    new['Lifetime'] = new['Lifetime'].astype(float)
    return new

#store the amount of earnings in 4 numpy arrays - containing earnings
# made respectively only in - OD, OW, EOW1, LT
def earnings(y):
    f = np.empty(0, dtype=float)
    s = np.empty(0, dtype=float)
    t = np.empty(0, dtype=float)
    fo = np.empty(0, dtype=float)
    #earnings_by_year = np.append(earnings_by_year, [0, 0, 0, 0], axis = 0)
    for x in range(1988, 2020):
        sum1 = y.loc[y['Release Date'] == x, 'Opening Day'].sum()
        sum2 = y.loc[y['Release Date'] == x, 'Opening Weekend'].sum() - sum1
        sum3 = y.loc[y['Release Date'] == x, 'End of Week 1'].sum()- sum2 - sum1
        sum4 = y.loc[y['Release Date'] == x, 'Lifetime'].sum() - sum3 - sum2 - sum1
        f = np.append(f, sum1)
        s = np.append(s, sum2)
        t = np.append(t, sum3)
        fo = np.append(fo, sum4)
    return f, s, t, fo

#modify all 3 databases
sk_new = modify(sk)
srk_new = modify(srk)
ak_new = modify(ak)

#get all 4 np arrays for all 3 actors
skod, skow, skew, sklt = earnings(sk_new)
srkod, srkow, srkew, srklt = earnings(srk_new)
akod, akow, akew, aklt = earnings(ak_new)

""" print(skod)
print(skow)
print(skew)
print(sklt)

print(skod)
print(skow)
print(skod.size)
print(srkod)
print(srkod.size)
print(akod)
print(akod.size) """

years = np.arange(1988, 2020)

plt.bar(years, skod)
plt.bar(years, skow, bottom=np.array(skod))
plt.bar(years, skew, bottom=np.array(skod)+np.array(skow))
plt.bar(years, sklt, bottom=np.array(skod)+np.array(skow)+np.array(skew))
plt.legend(["Opening Day", "Opening Week", 'End of Week 1', 'Lifetime Collection'])
plt.xlabel("Year", fontweight="bold")
plt.yticks(np.arange(0, 700, 100))
plt.ylabel("Box Office Collection in Rupees(Cr)", fontweight="bold")
plt.title("Distribution of SK's movies' collection over their running period",
          fontweight="bold")
#plt.show()
plt.savefig(os.path.join(pwd, 'Plots/skstack.png'), dpi=200)
plt.close()


plt.bar(years, srkod)
plt.bar(years, srkow, bottom=np.array(srkod))
plt.bar(years, srkew, bottom=np.array(srkod)+np.array(srkow))
plt.bar(years, srklt, bottom=np.array(srkod)+np.array(srkow)+np.array(srkew))
plt.legend(["Opening Day", "Opening Week",
            'End of Week 1', 'Lifetime Collection'])
plt.xlabel("Year", fontweight="bold")
plt.ylabel("Box Office Collection in Rupees(Cr)", fontweight="bold")
plt.yticks(np.arange(0, 700, 100))
plt.title("Distribution of SRK's movies' collection over their running period",
          fontweight="bold")
#plt.show()
plt.savefig(os.path.join(pwd, 'Plots/srkstack.png'), dpi=200)
plt.close()


plt.bar(years, akod)
plt.bar(years, akow, bottom=np.array(akod))
plt.bar(years, akew, bottom=np.array(akod)+np.array(akow))
plt.bar(years, aklt, bottom=np.array(akod)+np.array(akow)+np.array(akew))
plt.legend(["Opening Day", "Opening Week",
            'End of Week 1', 'Lifetime Collection'])
plt.xlabel("Year", fontweight="bold")
plt.ylabel("Box Office Collection in Rupees(Cr)", fontweight="bold")
plt.yticks(np.arange(0, 700, 100))
plt.title("Distribution of AK's movies' collection over their running period",
          fontweight="bold")
#plt.show()
plt.savefig(os.path.join(pwd, 'Plots/akstack.png'), dpi=200)
plt.close()
