import matplotlib.pyplot as plt
import numpy as np

c=input("Number of profile: ")
c=int(c)

for i in range(c):
    i=i+1
    a = input(f"Amplitude {i} : ")
    w = input(f"Frequency {i} : ")
    a=int(a)
    w=int(w)
    x= np.arange(0,2*np.pi,0.001)
    y=a*np.sin(w*x)

    plt.plot(x,y)
plt.ylabel('Amplitude')
plt.xlabel('X values from 0 to 2pi')
plt.title('Plot of sine from 0 to 2pi')
plt.legend(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"])
plt.show()

