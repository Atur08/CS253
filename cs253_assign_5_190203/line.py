#importing packages
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pwd = os.path.dirname(__file__)
#importing csv files using pandas
sk = pd.read_csv(open(os.path.join(pwd, 'Data/new_skdata.csv'), "r"))
srk = pd.read_csv(open(os.path.join(pwd, 'Data/new_srkdata.csv'), "r"))
ak = pd.read_csv(open(os.path.join(pwd, 'Data/new_akdata.csv'), "r"))

#function to return an array containing total earnings per year
def earnings(y):
    earnings_by_year = np.empty(0, dtype=float)
    for x in range(1988, 2020):
        sum = y.loc[y['Release Date'] == x, 'Lifetime'].sum()
        earnings_by_year = np.append(earnings_by_year, sum)
    return earnings_by_year

#function to change the type of Lifetime earnings to float from string 
#and also remove those rows which do not contain the info about Lifetime 
#earnings (i.e. contain "N.A")
def modify(y):
    new = y[y['Lifetime'] != "N.A"]
    new.Lifetime = new.Lifetime.astype(float)
    return new

#modify the data sets
sk_new = modify(sk)
srk_new = modify(srk)
ak_new = modify(ak)

#get total earnings per year
sk_earnings_by_year = earnings(sk_new)
srk_earnings_by_year = earnings(srk_new)
ak_earnings_by_year = earnings(ak_new)

#print(sk_earnings_by_year)

#32 years - 1988 to 2019 
years = np.arange(1988, 2020)

#line plot earning data of all 3 actors
plt.plot(years, sk_earnings_by_year, label="SK")
plt.plot(years, srk_earnings_by_year, label="SRK")
plt.plot(years, ak_earnings_by_year, label="AK")

plt.legend()

plt.xlabel("Year", fontweight="bold")
plt.ylabel("Earnings in Rupees(Cr)", fontweight="bold")
plt.title("Box Office Collections of 3 Khans of Bollywood for the last 30 years",
          fontweight="bold")

#plt.show()
plt.savefig(os.path.join(pwd, 'Plots/line.png'), dpi=200)
