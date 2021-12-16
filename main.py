import matplotlib.pyplot as plt
import numpy as np



c=input("Number of profile: ")
c=int(c)
total =0
for i in range(c):
    i=i+1
    a = input(f"Amplitude {i} : ")
    if "," in a:
        while True:
            a=input(f"Do not use ',' !\nAmplitude {i} :")
            if not "," in a:
                break
    a=float(a)

    w = input(f"Frequency {i} : ")
    w=float(w)
    x= np.arange(0,2*np.pi,0.001)
    y=a*np.sin(w*x)
    total+=y
    # plt.plot(x, y)
plt.plot(x,total)
plt.ylabel('Amplitude')
plt.xlabel('X values from 0 to 2pi')
plt.title('Plot of sine from 0 to 2pi')
# plt.legend()
plt.show()


