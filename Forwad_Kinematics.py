import sympy as sym #
import numpy as np  # Libraries import
import math as math        #
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

pi=math.pi


dof=7;#7 Degrees of freedom

q1,q2,q3,q4,q5,q6,q7=sym.symbols('q1,q2,q3,q4,q5,q6,q7')    #joint variable as symbolic
theta=[q1,q2,q3,q4,q5,q6,q7]                                #
d=[0,0,3,0,5,0,7]                                         # Denavit-Hartenberg parameters definition
alpha=[-pi/2,pi/2,-pi/2,pi/2,-pi/2,pi/2,0]                  #
a=[0,0,0,0,0,0,0]                                           #



def substitute(q1,q2,q3,q4,q5,q6,q7):

    T1=np.array([[math.cos(q1),-math.sin(q1)*math.cos(alpha[0]),math.sin(q1)*math.sin(alpha[0]),a[0]*math.cos(q1)],\
    [math.sin(q1),math.cos(q1)*math.cos(alpha[0]),-math.cos(q1)*math.sin(alpha[0]),alpha[0]*math.sin(q1)],\
    [0,math.sin(alpha[0]),math.cos(alpha[0]),d[0]],\
    [0,0,0,1]])


    T2=np.array([[math.cos(q2),-math.sin(q2)*math.cos(alpha[1]),math.sin(q2)*math.sin(alpha[1]),a[1]*math.cos(q2)],\
    [math.sin(q2),math.cos(q2)*math.cos(alpha[1]),-math.cos(q2)*math.sin(alpha[1]),alpha[1]*math.sin(q2)],\
    [0,math.sin(alpha[1]),math.cos(alpha[1]),d[1]],\
    [0,0,0,1]])


    T3=np.array([[math.cos(q3),-math.sin(q3)*math.cos(alpha[2]),math.sin(q3)*math.sin(alpha[2]),a[2]*math.cos(q3)],\
    [math.sin(q3),math.cos(q3)*math.cos(alpha[2]),-math.cos(q3)*math.sin(alpha[2]),alpha[2]*math.sin(q3)],\
    [0,math.sin(alpha[2]),math.cos(alpha[2]),d[2]],\
    [0,0,0,1]])


    T4=np.array([[math.cos(q4),-math.sin(q4)*math.cos(alpha[3]),math.sin(q4)*math.sin(alpha[3]),a[3]*math.cos(q4)],\
    [math.sin(q4),math.cos(q4)*math.cos(alpha[3]),-math.cos(q4)*math.sin(alpha[3]),alpha[3]*math.sin(q4)],\
    [0,math.sin(alpha[3]),math.cos(alpha[3]),d[3]],\
    [0,0,0,1]])

    T5=np.array([[math.cos(q5),-math.sin(q5)*math.cos(alpha[4]),math.sin(q5)*math.sin(alpha[4]),a[4]*math.cos(q5)],\
    [math.sin(q5),math.cos(q5)*math.cos(alpha[4]),-math.cos(q5)*math.sin(alpha[4]),alpha[4]*math.sin(q5)],\
    [0,math.sin(alpha[4]),math.cos(alpha[4]),d[4]],\
    [0,0,0,1]])

    T6=np.array([[math.cos(q6),-math.sin(q6)*math.cos(alpha[5]),math.sin(q6)*math.sin(alpha[5]),a[5]*math.cos(q6)],\
    [math.sin(q6),math.cos(q6)*math.cos(alpha[5]),-math.cos(q6)*math.sin(alpha[5]),alpha[5]*math.sin(q6)],\
    [0,math.sin(alpha[5]),math.cos(alpha[5]),d[5]],\
    [0,0,0,1]])

    T7=np.array([[math.cos(q7),-math.sin(q7)*math.cos(alpha[6]),math.sin(q7)*math.sin(alpha[6]),a[6]*math.cos(q7)],\
    [math.sin(q7),math.cos(q7)*math.cos(alpha[6]),-math.cos(q7)*math.sin(alpha[6]),alpha[6]*math.sin(q7)],\
    [0,math.sin(alpha[6]),math.cos(alpha[6]),d[6]],\
    [0,0,0,1]])

    return T1,T2,T3,T4,T5,T6,T7;

def matMultiplication(T1,T2,T3,T4,T5,T6,T7):
    T1_2=np.dot(T1,T2)
    T1_3=np.dot(T1_2,T3);
    T1_4=np.dot(T1_3,T4);
    T1_5=np.dot(T1_4,T5);
    T1_6=np.dot(T1_5,T6);
    T1_7=np.dot(T1_6,T7);
    return T1_7;

if __name__ == '__main__':
    fig=plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for q1 in range(-90,90,18):
        for q2 in range(-90,90,18):
            for q3 in range(-90,90,18):
                for q4 in range(-90,90,18):
                    T1,T2,T3,T4,T5,T6,T7=substitute(q1,q2,q3,q4,0,0,0)
                    T1_7=matMultiplication(T1,T2,T3,T4,T5,T6,T7)
                    #print(T1_7)
                    x=T1_7[0,3]
                    y=T1_7[1,3]
                    z=T1_7[2,3]
                    ax.scatter(x, y, z,c='r',marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
