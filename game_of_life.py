# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 18:34:47 2021

@author: Lyth Mashni
"""
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.sparse import dia_matrix
import argparse
#from PIL import Image
#from matplotlib import animation, rc
#from IPython.display import HTML

###### If your here for the first time

###### run once for animation
	
###### otherwise please check jupyter notebook to make more sense of this. 


###### when run as main this routine should preduces an animation of connways game of life
###### it contains several implimatations and initail conditions. Though the difult is the most ###### efficient. The functions are flexible enough to be used for other applications
###### when imported this script contains useful funtions for applications in graph theory and ###### simulation.

					


# this emmbeds an initial matrix in to a bigger playing field

def emb_mat(Z,d):
    d2=int(d/2)
    y = np.zeros((d,d))
    a,b = int(Z.shape[0]/2),int(Z.shape[1]/2)
    a1 ,a2 = int(np.floor(Z.shape[0]/2)) , int(np.ceil(Z.shape[0]/2))
    b1 ,b2 = int(np.floor(Z.shape[1]/2)) , int(np.ceil(Z.shape[1]/2))
    y[d2-a1:d2+a2,d2-b1:d2+b2]= Z
    
    return y
    
# this function returns a 2d matrix with the number of neighrest neighbors.
# it usese rolls to do the calculation    
def NN_roll(Z,M=1):
    
    D = np.zeros(np.shape(Z))
    D+= np.roll(Z, -1, axis = 1)
    D+=np.roll(Z, 1, axis = 1)
    D+=np.roll(Z, -1, axis = 0)
    D+= np.roll(Z, 1, axis = 0)
    D+=np.roll(np.roll(Z, -1, axis = 0), -1, axis = 1)
    D+=np.roll(np.roll(Z, 1, axis = 0), -1, axis = 1)
    D+=np.roll(np.roll(Z, 1, axis = 0), 1, axis = 1)
    D+=np.roll(np.roll(Z, -1, axis = 0), 1, axis = 1)
    
    return D
    
    
# this function sets up an adjecancy matrix. to be used to get the number of nearest neighbours more efficiently.


def adj_mat(d):
    
    m1= np.zeros(d**2)
    m1[1],m1[-1] = 1,1
    m1[d]=1
    m1[-d]=1
    m1[1+d]=1
    m1[-1+d]=1
    m1[1-d]=1
    m1[-1-d]=1
    ofs1 = np.arange(d**2)[m1==1]
    ofs = np.zeros(len(ofs1)*2)
    ofs[:len(ofs1)]= ofs1
    ofs[len(ofs1):]=-ofs1
    
    data = np.expand_dims(np.ones(d**2),0).repeat(len(ofs), axis=0)
    return dia_matrix((data, ofs), shape=(d**2, d**2))

 
    

#this function finds the number of nearst neighbours using the adj_mat
def NN_adj(c,adj):
    l=len(c)
    c_=c.reshape(c.size)
    return adj.dot(c_).reshape((l,l))


# makes mask for convolution

def Mask(d):
    msk = np.zeros((d,d))
    d2 = int(d/2)
    x = np.array([[1,1,1],[1,0,1],[1,1,1]])
    msk[d2-1:d2+2,d2-1:d2+2]=x
    return msk
    
def NN_conv(Z,Msk_):
    Z_ = np.fft.fft2(Z)
    
    nn_ = np.fft.ifft2(Z_*Msk_)
    
    return np.round(nn_.real)


# given the number of nearest neighbour this applies the selected rules. 
def rule(Z,nn,actions,f,*args):
    D =f(Z,*args)
    for k,v in zip(actions,nn):
        if k != 2:
            Z[D == v] = k
    return Z
   
    
def game_of_life(Z,steps,nn,actions,time_it,f,*args):
    d = len(Z)
    
    if time_it == False:
        arr=np.zeros((steps,d,d))


        arr[0,:,:] = Z

        t0 = time.time()
        for i in range(1,steps):
            arr[i,:,:]= rule((arr[i-1,:,:]),nn,actions,f,*args) 
            if i %int(steps/5) == 0:
                print('step', i)
            i = i + 1
        t = time.time()-t0    
        print('this took:',str(int(t*1e4)/1e4) ,'seconds for',str(steps),'steps')
        return arr
    else:
        t0 = time.time()
        for i in range(1,steps):
            Z= rule(Z,nn,actions,f,*args) 
        t = time.time()-t0 
        print('this took:',str(int(t*1e4)/1e4) ,'seconds for',str(steps),'steps')
        
        
    

def animate(arr,steps):  
    fig,ax = plt.subplots(figsize=(10,10))
    ims=[]
    plt.rcParams["figure.figsize"] = (30,30)
    for i in range(steps):
        im = ax.imshow(arr[i],animated = True)
        ims.append([im])
    return animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
    
def arguments_parser():
	parser = argparse.ArgumentParser(description="This preduces an animation of the game of life the flag -i choses and initial setup from the initial set up dictionary. -d sets the dimentions of the playing field and -s sets the number of iterations")
	parser.add_argument('-i', type=str,default='pento',help="initial condition")
	parser.add_argument('-d', type=int,default=128,help="resolution")
	parser.add_argument('-s', type=int,default=1000,help="number of steps")
	return parser.parse_args()   
if __name__ == '__main__' :  



#### some choices of initial conditions #####
    grower = np.array(
            [ [0,0,0,0,0],
              [0,0,1,1,0],
              [0,1,1,0,0],
              [0,0,1,0,0],
              [0,0,0,0,0]]
            ) 

    periodic = np.array(
            [ [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,1,0,0,0,0,0],
              [0,0,0,0,1,1,1,0,0,0,0],
              [0,0,0,1,1,1,1,1,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,1,1,1,1,1,0,0,0],
              [0,0,0,0,1,1,1,0,0,0,0],
              [0,0,0,0,0,1,0,0,0,0,0]]
            )

    floater = np.array(
            [ [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,1,1,0,0,0,0],
              [0,0,0,0,0,1,0,1,0,0,0],
              [0,0,0,0,0,1,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0]]
            )
   
    init_dict = {'pento':grower,'peri15':periodic,'floater':floater}
    args = arguments_parser()

    # you can run the game with diffrent rules. This is the setting for connway Game of life
    
    nn      = np.array([0,1,2,3,4,5,6,7,8]) 
    actions = np.array([0,0,2,1,0,0,0,0,0])
    
    steps =args.s        #number of steps
    d =args.d  	#dimentions of field
    init = init_dict[args.i]
    X = emb_mat(init,d) # emmbed initial matrix into larger field
    
    ## this mask is for the convolution maethod
    Msk_ = np.roll(Mask(d),int(d/2),0)
    Msk_ = np.roll(Msk_,int(d/2),1)
    Msk_ = np.fft.fft2(Msk_)  
    
    ## this sets up the adjacency matrix
    adj = adj_mat(d)

    arr = game_of_life(X,10000,nn,actions,0,NN_adj,adj)

    anim = animate(arr,steps)

    plt.show()
'''
print('rolling method')
arr = game_of_life(X,10000,nn,actions,1,NN_roll,1)
print('using adjecancy matrix')
arr = game_of_life(X,10000,nn,actions,1,NN_adj,adj)
print('using convolution')
arr = game_of_life(X,10000,nn,actions,1,NN_conv,Msk_)

'''

