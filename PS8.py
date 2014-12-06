#SMILEY FACE
import numpy as np
import matplotlib.pyplot as plt
#Plotting NPV vs t
def projectA(k):
    NPVA = (-3500)+(800/(1+k)**1)+(800/(1+k)**2)+(800/(1+k)**3)+(800/(1+k)**4)+(800/(1+k)**5)+(800/(1+k)**6)+(800/(1+k)**7)+(800/(1+k)**8)
    return NPVA

def projectB(k):
    NPVB = (-5000)+(2000/(1+k)**1)+(1500/(1+k)**2)+(1500/(1+k)**3)+(500/(1+k)**4)+(500/(1+k)**5)+(1500/(1+k)**6)
    return NPVB

def projectC(k):
    NPVC = (-7500)+(2000/(1+k)**1)+(2000/(1+k)**2)+(2000/(1+k)**3)+(4000/(1+k)**4)+(5000/(1+k)**5)
    return NPVC

def projectD(k):
    NPVD = (-4000)+(5000/(1+k)**1)+(3000/(1+k)**2)+(-2500/(1+k)**3)+(-2000/(1+k)**4)+(1000/(1+k)**5)+(2000/(1+k)**6)+(3000/(1+k)**7)
    return NPVD

k = np.linspace(0.01,0.60,200)
projectAvec = projectA(k)
projectBvec = projectB(k)
projectCvec = projectC(k)
projectDvec = projectD(k)

plt.figure(1)
plt.plot(k,projectAvec,label='Project A')
plt.plot(k,projectBvec,label='Project B')
plt.plot(k,projectCvec,label='Project C')
plt.plot(k,projectDvec,label='Project D')
plt.xlabel('Discount Rate (Decimal)')
plt.ylabel('NPV ($)')
plt.legend(loc='upper right')
plt.grid(b=True, which='major', color='b', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='-')
plt.minorticks_on()
plt.show()
