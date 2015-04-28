# Tutorial 4, part 3

#From my Tutorial 4 Part 1, Convolution

import numpy
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt


#Function
def conv(x,i=0):
    vector=x*0
    vector[i]=1
    fourierft=fft(vector)
    xft=fft(x)
    return numpy.real(ifft(xft*fourierft))
   

#From my Tut 4, part 2

# Tutorial 4, part 2

def correlation(x,y):
    xft= fft(x)
    yft= fft(y)
    conj_yft=numpy.conj(yft)
    return numpy.real(ifft(xft*conj_yft))    

if __name__=='__main__':
    x=numpy.arange(-30,30,0.1)
    s=2
    y=numpy.exp(-0.5*x**2/s**2)
    y_y=correlation(y,y)
    #shift with an arb amount
    y_size=y.size/10
    shift=conv(y,y_size)
    shift_correlation=correlation(shift,shift)
    #Plot
    plt.plot(x,y_y)
    plt.plot(x,shift_correlation)
    plt.show()
