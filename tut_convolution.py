#Tutorial 4, Convolution

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
    

if __name__=='__main__':
#Variables
    x= numpy.arange(-20,20,0.1)
    s=2
    y= numpy.exp(-0.5*x**2/(s**2))
    N=y.size
#Shift
    yshift = conv(y,N/2)
    
    plt.ion()
    plt.plot(x,y)
    plt.plot(x,yshift)
