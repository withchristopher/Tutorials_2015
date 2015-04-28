# Tutorial 4, part 2

import numpy
from matplotlib import pyplot as plt
from numpy.fft import fft,ifft
import time
t=time.time()

def correlation(x,y):
    xft= fft(x)
    yft= fft(y)
    conj_yft=numpy.conj(yft)
    return numpy.real(ifft(xft*conj_yft))    

if __name__=='__main__':
   x= numpy.arange(-10,20,0.1)
   s=2
   y=numpy.exp(-0.5*x**2/s**2)

#Plotting

   y_y=correlation(y,y)
   plt.plot(x,y_y)
   plt.show()
