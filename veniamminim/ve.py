import math

# Assuming HalfPi is defined as half of Pi
HalfPi = math.pi / 2

# Example angle sa
sa = 2.7  # in radians

# Aligning sa to the nearest multiple of HalfPi
s = sa - sa % HalfPi + HalfPi

print(s)  # This would print the aligned value
