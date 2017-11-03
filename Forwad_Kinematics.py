# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:46:51 2017

@author: gerha
"""
import sympy as sym #
import numpy as np  # Libraries import
import math as math        #
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

pi=math.pi

dof=7;

q1,q2,q3,q4,q5,q6,q7=sym.symbols('q1,q2,q3,q4,q5,q6,q7')    #joint variable as symbolic
d3=3
d5=5
d7=7

#Robot dictionary
robot=\
{1:[q1,0,-pi/2,0],\
 2:[q2,0,pi/2,0],\
 3:[q3,d3,-pi/2,0],\
 4:[q4,0,pi/2,0],\
 5:[q5,d5,-pi/2,0],\
 6:[q6,0,pi/2,0],\
 7:[q7,d7,-pi/2,0],}

def substitute(q1,q2,q3,q4,q5,q6,q7):
    T=[]
    q=[q1,q2,q3,q4,q5,q6,q7];
    for i in range(0,dof):
        currentJoint=robot.get(i+1)
        currentJoint[0]=q[i]
        #currentJoint[0]=0
        mat=np.array([[math.cos(currentJoint[0]),-math.sin(currentJoint[0])*math.cos(currentJoint[2]),math.sin(currentJoint[0])*math.sin(currentJoint[2]),currentJoint[3]*math.cos(currentJoint[0])],\
                            [math.sin(currentJoint[0]),math.cos(currentJoint[0])*math.cos(currentJoint[2]),-math.cos(currentJoint[0])*math.sin(currentJoint[2]),currentJoint[2]*math.sin(currentJoint[0])],\
                            [0,math.sin(currentJoint[2]),math.cos(currentJoint[2]),currentJoint[1]],\
                            [0,0,0,1]])
        T.append(mat)
    return T

def matMultiplication(T):
    for i in range(1,dof):
        if i==1:
            matMult=np.dot(T[i-1],T[i])
        else:
            matMult=np.dot(matMult,T[i])
    return matMult    
    
    
if __name__ == '__main__':
    fig=plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for q1 in range(-180,180,1):
        for q2 in range(-180,180,1):
                T=substitute(q1,q2,0,0,0,0,0)
                T1_7=matMultiplication(T)
                x=T1_7[0,3]
                y=T1_7[1,3]
                z=T1_7[2,3]
                ax.scatter(x, y, z,c='r',marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
            
    plt.show()
    T=substitute(0,0,0,0,0,0,0)
    T1_7=matMultiplication(T)
    print(len(T))
    print(T1_7)
    print(T)