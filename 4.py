import math
import statistics

# Math Module
num1 = 25
print("Square root of", num1, ":", math.sqrt(num1))
print("Ceiling of 4.3:", math.ceil(4.3))
print("Floor of 4.8:", math.floor(4.8))
print("Sine of 30 degrees:", math.sin(math.radians(30)))
print("Cosine of 45 degrees:", math.cos(math.radians(45)))
print("e^2:", math.exp(2))
print("Logarithm base 10 of 100:", math.log10(100))
print("Value of pi:", math.pi)
print("Value of e:", math.e)

# Statistics Module
data = [1, 2, 2, 3, 4, 4, 5]
print("\nMean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Variance:", statistics.variance(data))
print("Standard Deviation:", statistics.stdev(data))

data_harmonic = [1, 2, 3, 4, 5]
print("Harmonic Mean:", statistics.harmonic_mean(data_harmonic))
print("Geometric Mean:", statistics.geometric_mean(data_harmonic))
