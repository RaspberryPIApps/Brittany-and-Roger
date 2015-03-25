How to Calculate Distance Using Wifi
=======================================================
Note: this research is a work in progress. Here are our findings:

a. we need three wifi access points.
b. The robot needs some device to be capable of receiving wifi signals and
calculating the strength of the signal (in dB).
c. We will use the formulas: FSPL:(dB) = 20log10(d)+20log10(f) -27.55 
d. units: MHz for frequency and meters for distance

PROBLEMS: 
a. FSPL requires free-space for calculation
b. We should sample the signal strength +10 times to account
for interference

1. python code to calculate the distance from ONE access point:
```python
import math
freqInMHz = somenumber
levelinDb = somenumberalso

results = (27.55 - (20 * math.log10(freqInMHz) + math.fabs(levelInDb)) / 20.0
math.pow(10.0, x)

print results
```

2. This code would be expanded to draw results for the next two access points.
Once we have all three distance, we can estimate the robot's position in the 
plane using trilateration or triangulation.

Refrences & Helpfull Links:
http://rvmiller.com/2013/05/part-1-wifi-based-trilateration-on-android/
http://ws2.binghamton.edu/fowler/Improving%20WLAN-Based%20Indoor%20Mobile%20Positioning%20Using%20Sparsity.pdf
https://www.youtube.com/watch?v=KSg2WN8EiKI
