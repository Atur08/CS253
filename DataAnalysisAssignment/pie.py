import os 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pwd = os.path.dirname(__file__)
sk = pd.read_csv(open(os.path.join(pwd, 'Data/new_skdata.csv'), "r"))
srk = pd.read_csv(open(os.path.join(pwd, 'Data/new_srkdata.csv'), "r"))
ak = pd.read_csv(open(os.path.join(pwd, 'Data/new_akdata.csv'), "r"))

#print(sk.Verdict.value_counts())
labels = sk.Verdict.unique() #get all the different verdicts that are there
plt.pie(sk.Verdict.value_counts(), labels=labels, autopct='%.2f') 
plt.title("Salman Khan Movies' Performance", fontweight="bold")
#plt.show()
plt.savefig(os.path.join(pwd, 'Plots/skpie.png'), dpi=200)
plt.close()

#print(srk.Verdict.value_counts())
labels = srk.Verdict.unique()
plt.pie(srk.Verdict.value_counts(), labels=labels, autopct='%.2f')
plt.title("Shah Rukh Khan Movies' Performance", fontweight="bold")
#plt.show()
plt.savefig(os.path.join(pwd, 'Plots/srkpie.png'), dpi=200)
plt.close()

#print(ak.Verdict.value_counts())
labels = ak.Verdict.unique()
plt.pie(ak.Verdict.value_counts(), labels=labels, autopct='%.2f')
plt.title("Aamir Khan Movies' Performance", fontweight="bold")
#plt.show()
plt.savefig(os.path.join(pwd, 'Plots/akpie.png'), dpi=200)
plt.close()
