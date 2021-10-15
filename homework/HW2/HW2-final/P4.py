# part 4
#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import datetime 

#worked with Angel Hsu

### Closure defined up here

currentDT = datetime.datetime.now()
hour = currentDT.hour
minute = currentDT.minute
second = currentDT.second


# Calculate theta in degrees for each hand

rad = np.pi/180

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



# Specify the length of hour, minute and second hands
#specified above

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


fig = plt.figure(figsize = (6,6))
plt.plot([0,x_s], [0,y_s], 'r-',label = 'Second Hand')
plt.plot([0,x_m], [0,y_m], 'g-',label = 'Minute Hand', linewidth = 3.5)
plt.plot([0,x_h], [0,y_h], 'b-',label = 'Hour Hand', linewidth = 3.5)
plt.title("Clock Not Digital")
plt.legend()
plt.axis([xmin,xmax,ymin,ymax])
plt.show()
