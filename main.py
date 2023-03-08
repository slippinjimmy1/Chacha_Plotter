import numpy as np
import matplotlib.pyplot as veryCoolPlotter

fig = veryCoolPlotter.figure(figsize = (8, 6))


x1 = np.linspace(-100,100,1000)


y1 = 0*x1


y2 = np.linspace(-100,100,1000)


x2 = 0*y2


veryCoolPlotter.plot(x1,y1)


veryCoolPlotter.plot(x2,y2)


x = np.linspace(-100,100,1000)

print("Make your expression in the form y = c - ax / b\n")

c, a, b = input("Enter values of c, a and b separated by spaces:").split()

y = ( int(c) - int(a)*x ) / int(b)

veryCoolPlotter.plot(x,y)

veryCoolPlotter.show()

