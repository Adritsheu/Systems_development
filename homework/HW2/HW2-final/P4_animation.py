#Part 4c Animation

#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import datetime 
from IPython.display import clear_output



# Specify the length of hour, minute and second hands
#specified above

x = 0
rad = np.pi/180
   
while x < 10: #want to run it for only 10 seconds
    currentDT = datetime.datetime.now()
    hour = currentDT.hour
    minute = currentDT.minute
    second = currentDT.second
    fig = plt.figure(figsize = (6,6))


    # Calculate theta in degrees for each hand
    theta_h = 90-30 * hour - minute/2 # hours
    theta_m = 90 - 6*minute # minutes
    theta_s = 90 - 6*second # seconds

    #hour positions
    rh = 15
    theta_rh = rad*theta_h #convert to radians for hour hand

    #minute positions
    rm = 20
    theta_rm = rad*theta_m
    #second positions
    rs = 25
    theta_rs = rad*theta_s
    #create our closure
    def length_clock(r):
        def clock_hand(theta):
            x = r*np.cos(theta)
            y = r*np.sin(theta)
            return x,y 
        return clock_hand

       
    hour_hand = length_clock(rh)
    x_h, y_h = hour_hand(theta_rh)


    min_hand = length_clock(rm)
    x_m, y_m = min_hand(theta_rm)


    sec_hand = length_clock(rs)
    x_s, y_s = sec_hand(theta_rs)
    
    # Plot the clock
    xmin = -30
    xmax = 30
    ymin = -30
    ymax = 30


    
    plt.plot([0,x_s], [0,y_s], 'r-',label = 'Second Hand')
    plt.plot([0,x_m], [0,y_m], 'g-',label = 'Minute Hand', linewidth = 3.5)
    plt.plot([0,x_h], [0,y_h], 'b-',label = 'Hour Hand', linewidth = 3.5)
    plt.title("Clock Not Digital")
    #plt.show()
    plt.axis([xmin,xmax,ymin,ymax])
    x+=1

    fig.canvas.draw()
    plt.pause(1)
    plt.cla()
    
    
    

    


    
