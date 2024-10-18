def wc(TdegC, windKPH):
   """
    * Calculates the wind chill, given
    * TdegC: the temp in degrees C
    * windKPH: the wind speed in km/h
    *
    * Returns:
    * vTemp: Wind chill in degrees C
   """
   vTemp = (0.6215 * TdegC) + 13.12
   vTemp = vTemp - 11.37 * windKPH**0.16
   vTemp = vTemp + 0.3965 * TdegC * windKPH**0.16

   return vTemp

T = -5.0
W = 10.0
print("WC=%8.3f T=%8.3f W=%6.3f km/h" % (wc(T, W), T, W))
if wc(T, W) <= 0 and wc(T, W) > -10:
  print("Low risk")
elif wc(T, W) <= -10 and wc(T, W) > -28:
  print("Moderate risk of hypothermia.")
elif wc(T, W) <= -28 and wc(T, W) > -40:
  print("High risk of frostbite.")
elif wc(T, W) <= -40 and wc(T, W) > -48:
  print("Severe risk of frostbite: exposed skin freezes in 5-10 minutes")
elif wc(T, W) <= -48 and wc(T, W) > -55:
  print("Severe risk of frostbite: exposed skin freezes in 2-5 minutes")
elif wc(T, W) <= -55:
  print("Extreme risk: exposed skin freezes in under 2 minutes")
  

T = -20.0
W = 20.0
print("WC=%8.3f T=%8.3f W=%6.3f km/h" % (wc(T, W), T, W))
if wc(T, W) <= 0 and wc(T, W) > -10:
  print("Low risk")
elif wc(T, W) <= -10 and wc(T, W) > -28:
  print("Moderate risk of hypothermia.")
elif wc(T, W) <= -28 and wc(T, W) > -40:
  print("High risk of frostbite.")
elif wc(T, W) <= -40 and wc(T, W) > -48:
  print("Severe risk of frostbite: exposed skin freezes in 5-10 minutes")
elif wc(T, W) <= -48 and wc(T, W) > -55:
  print("Severe risk of frostbite: exposed skin freezes in 2-5 minutes")
elif wc(T, W) <= -55:
  print("Extreme risk: exposed skin freezes in under 2 minutes")
  
T = -45.0
W = 40.0
print("WC=%8.3f T=%8.3f W=%6.3f km/h" % (wc(T, W), T, W))
if wc(T, W) <= 0 and wc(T, W) > -10:
  print("Low risk")
elif wc(T, W) <= -10 and wc(T, W) > -28:
  print("Moderate risk of hypothermia.")
elif wc(T, W) <= -28 and wc(T, W) > -40:
  print("High risk of frostbite.")
elif wc(T, W) <= -40 and wc(T, W) > -48:
  print("Severe risk of frostbite: exposed skin freezes in 5-10 minutes")
elif wc(T, W) <= -48 and wc(T, W) > -55:
  print("Severe risk of frostbite: exposed skin freezes in 2-5 minutes")
elif wc(T, W) <= -55:
  print("Extreme risk: exposed skin freezes in under 2 minutes")
