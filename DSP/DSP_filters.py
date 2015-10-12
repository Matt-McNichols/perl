import argparse

import math
import numpy as np
from scipy import signal
import scipy.io.wavfile
import matplotlib.pyplot as plt

def filtdec(x_array, h_filter, downsample):  
    
    q = []    
    
    N = len(x_array) 
    
     #mirror the array
    for i in range(N-1, -1, -1):
        x_array.append(x_array[i])    
    
    #convolve the signal with filter
    y = scipy.signal.convolve(x_array,h_filter, 'same')
    
    #downsample the array
    for i in range(0   ,   int(len(y)/2)  ):
        q.append(y[2*i])
    return q

def upfilt(x_array, h_filter, upsample):
    
    q = []
    
    for i in range(0, 2*len(x_array)):
        if(i%2):
            q.append(x_array[int(i/2)])
        else:
            q.append(0)
             
    y = scipy.signal.convolve(q, h_filter, 'same')
    
    
    return y 


def IFT(length):
    
    q = np.zeros(length) 
    increment = (2*math.pi)/length    
    
    for i in range(0,length):        
        v = ((-1/4)*(math.cos(2*i*increment))+((1/2)*math.cos(i*increment))+(3/4))                
        q[i] = v
        
    return q


def main():
    fs, x = scipy.io.wavfile.read("beat.wav")    
    
    h1 = [0,1,0]
    h2 = [1,0,1]
    x = []
    for i in range(0,10):
        x.append(i)

    x = filtdec(x,h1, 2)
    print(x)
    
    x = upfilt(x, h2, 2)
    print(x)
    
    print(IFT(10))
       
    print('end')
    
if __name__ == "__main__":
    main()
    
   
   
   
   
   
   
   
   
    
    
    '''
        # Parse command-line arguments
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("--order", type=int, default=3, help="order of Bessel function")
    parser.add_argument("--output", default="plot.png", help="output image file")
    args = parser.parse_args()

    # Compute maximum
    f = lambda x: -special.jv(args.order, x)
    sol = optimize.minimize(f, 1.0)

    # Plot
    x = np.linspace(0, 10, 5000)
    #plt.plot(x, special.jv(args.order, x), '-', sol.x, -sol.fun, 'o')

    # Produce output
    #plt.savefig(args.output, dpi=96)
'''
