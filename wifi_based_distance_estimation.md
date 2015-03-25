How to Calculate Distance Using Wifi
=======================================================
*This research is a work in progress. Here are our findings:*

* We need three wifi access points.
* The robot needs some device capable of receiving wifi signals and calculating the strength of the signal (in dB).
* We will use the formulas: FSPL:(dB) = 20log10(d)+20log10(f) -27.55 
* Units: MHz for frequency and meters for distance

**Problems:**
* FSPL requires free-space for calculation.
* We should sample the signal strength +10 times to account for interference.

**Python code to calculate the distance from ONE access point:**
```python
import math
freqInMHz = somenumber
levelinDb = somenumberalso

results = (27.55 - (20 * math.log10(freqInMHz) + math.fabs(levelInDb)) / 20.0
math.pow(10.0, x)

print results
```

This code would be expanded to draw results for the next two access points.
Once we have all three distance, we can estimate the robot's position in the 
plane using trilateration or triangulation.

**Refrences & Helpfull Links:**

* http://rvmiller.com/2013/05/part-1-wifi-based-trilateration-on-android/
* http://ws2.binghamton.edu/fowler/Improving%20WLAN-Based%20Indoor%20Mobile%20Positioning%20Using%20Sparsity.pdf
* https://www.youtube.com/watch?v=KSg2WN8EiKI
