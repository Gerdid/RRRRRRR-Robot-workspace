# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:46:51 2017

@author: gerha
"""
import sympy as sym                     #
import numpy as np                      #
import math as math                     #Libraries import
from mpl_toolkits.mplot3d import Axes3D #
import matplotlib.pyplot as plt         #

#---Constants definition---#
pi=math.pi
dof=7;      #Definition of DOF of robot
q1,q2,q3,q4,q5,q6,q7=sym.symbols('q1,q2,q3,q4,q5,q6,q7')    #joint variable as symbolic
d3=3        #
d5=5        #Distance between joints (depending on desing)
d7=7        #
minAngle=-90    #Minimum reacheale angle by the joint
maxAngle=91     #Maximum reachable angle by the joint
stepSize=10      #Degrees between each joint movement


#Robot dictionary
#key:number of joint
#[theta,d,alpha,a]
robot=\
{1:[q1,0,-pi/2,0],\
 2:[q2,0,pi/2,0],\
 3:[q3,d3,-pi/2,0],\
 4:[q4,0,pi/2,0],\
 5:[q5,d5,-pi/2,0],\
 6:[q6,0,pi/2,0],\
 7:[q7,d7,0,0]}

def substitute(q1,q2,q3,q4,q5,q6,q7):
    T=[0,0,0,0,0,0,0]
    q=[math.radians(q1),math.radians(q2),math.radians(q3),math.radians(q4),math.radians(q5),math.radians(q6),math.radians(q7)];     #degrees to radian
    #Evaluation for each joint according to the transformation formula
    for i in range(0,dof):
        currentJoint=robot.get(i+1)
        currentJoint[0]=q[i]
        mat=np.array([[np.cos(q[i]),-np.sin(q[i])*np.cos(currentJoint[2]),np.sin(q[i])*np.sin(currentJoint[2]),currentJoint[3]*np.cos(q[i])],\
                            [np.sin(q[i]),np.cos(q[i])*np.cos(currentJoint[2]),-np.cos(q[i])*np.sin(currentJoint[2]),currentJoint[3]*np.sin(q[i])],\
                            [0,np.sin(currentJoint[2]),np.cos(currentJoint[2]),currentJoint[1]],\
                            [0,0,0,1]])
        T[i]=mat
    return T;

def matrixMultiplication(T):
    for i in range(0,dof-1):
        if i==0:
            matMult=np.dot(T[i],T[i+1])
            temp=matMult
        else:
            matMult=np.dot(temp,T[i+1])
            temp=matMult
    return temp;

if __name__ == '__main__':

    #-----Workspace-----#

    fig=plt.figure()
    fig.suptitle('WORKSPACE')


    ax = fig.add_subplot(111, projection='3d')


    #Only first two joint variables neccesary for maximum robot workspace
    for q1 in range(minAngle,maxAngle,stepSize):
        for q2 in range(minAngle,maxAngle,stepSize):
            T=substitute(q1,q2,0,0,0,0,0)
            T0_7=matrixMultiplication(T)
            #Obtain the translation vector from the transformation matrix
            x=T0_7[0,3]
            y=T0_7[1,3]
            z=T0_7[2,3]

            ax.scatter(x, y, z,c='orange',marker='o')


    #Graph workspace
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


    #-----Orientation-----#
    figRot=plt.figure()
    figRot.suptitle('END EFFECTOR ORIENTATION')

    rot= figRot.add_subplot(111)

    #Q7 is redundant so it is not considered
    for q4 in range(minAngle,maxAngle,stepSize):
        for q5 in range(minAngle,maxAngle,stepSize):
            for q6 in range(minAngle,maxAngle,stepSize):
                T=substitute(0,0,0,q4,q5,q6,0)
                T0_7=matrixMultiplication(T)
                #From the transformation matrix obtain the 3x3 rotation matrix
                T_Rot=np.array([[T0_7[0,0],T0_7[0,1],T0_7[0,2]],\
                                [T0_7[1,0],T0_7[1,1],T0_7[1,2]],
                                [T0_7[2,0],T0_7[2,1],T0_7[2,2]]])
                #Multiply rotation matrix by a unitary vector
                xyz_Rot=np.dot(T_Rot,np.array([[1/math.sqrt(3)],[1/math.sqrt(3)],[1/math.sqrt(3)]]))
                x_Rot=xyz_Rot[0];   #x is the first element from the previous routine
                y_Rot=xyz_Rot[1];   #y is the second element
                z_Rot=xyz_Rot[2];   #z is the third element

                rot.scatter(x_Rot, y_Rot,c='coral',marker='o',s=1)

    #Graph rotation
    rot.set_xlabel('X')
    rot.set_ylabel('Y')
    #rot.set_zlabel('Z')

    plt.show()
