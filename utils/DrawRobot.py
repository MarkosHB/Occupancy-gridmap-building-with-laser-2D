import numpy as np
import matplotlib.pyplot as plt

def DrawRobot(fig, ax, pose, axis_percent, color='red', linewidth=.5, **kwargs):
# This function draws a triangle representing a robot at pose Xr (x,y,theta, using the color 'col' 
# This code has been taken/adapted from  P. Newman http://www.robots.ox.ac.uk/~pnewman
    a=plt.axis()
    l1=axis_percent*(a[1]-a[0])
    l2=axis_percent*(a[3]-a[2])
    P=np.array([[-1,1,0,-1],[-1,-1, 3,-1]])#basic triangle
    theta = pose[2, 0]-np.pi/2#rotate to point along x axis (theta = 0)
    c=np.cos(theta)
    s=np.sin(theta)
    P=np.array([[c,-s],[s, c]])@P #rotate by theta
    P[0,:]=P[0,:]*l1+pose[0, 0] #scale and shift to x
    P[1,:]=P[1,:]*l2+pose[1, 0]
    h = ax.plot(P[0,:],P[1,:], color=color, linewidth=linewidth, **kwargs)# draw
    #hold on,
    ax.plot(pose[0, 0],pose[1, 0],'+',color=color, markersize=(3*linewidth +1), linewidth=linewidth)
    
    return h
