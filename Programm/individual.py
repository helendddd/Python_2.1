from math import pi

R = float(input("Enter outer radius... "))
r = float(input("Enter inner radius... "))

print("Ring ares is ", f"{pi * (R - r):.2f}")
