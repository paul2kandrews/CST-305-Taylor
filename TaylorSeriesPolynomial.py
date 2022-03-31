import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.special import factorial as fact

def part1A(x, x0):
    def y(x):
        return 1
    def dy(x):
        return -1
    def d2y(x):
        return 2*x*dy(x) - x**2*y(x)
    def d3y(x):
        return 2*x*d2y(x) + 2*dy(x) - x**2*dy(x) - 2*x*y(x)
    def d4y(x):
        return 2*x*d3y(x) + 4*d2y(x) - x**2*d2y(x) - 4*x*dy(x) - 2*y(x)
    
    return y(x0) + (dy(x0)/1)*(x-x0) + (d2y(x0)/2)*(x-x0)**2 + (d3y(x0)/6)*(x-x0)**3 + (d4y(x0)/24)*(x-x0)**4

def part1B(x, x0):
    def y(x):
        return 6
    def dy(x):
        return 1
    def d2y(x):
        return dy(x)*(x-2)-2*y(x)
    
    return y(x0) + (dy(x0)/1)*(x-x0) + (d2y(x0)/2)*(x-x0)**2

def part2(x, a0, a1):
    a = a0*(((-1/8)*pow(x, 2)) + ((1/128)*pow(x, 4)) + ((13/15360)*pow(x, 6)) + ((403/3440640)*pow(x, 8)) + ((-247/1843200)*pow(x, 10)))
    b = a1*(x + ((-1/24)*pow(x, 3)) + ((7/1920)*pow(x, 5)) + ((-7/15360)*pow(x, 7)) + ((43/61440)*pow(x, 9)))
    return a + b

print(part1A(3.5, 0))
print(part1B(3, 3))
print(part2(0, 1, 2))

dt = 0.02
num_steps = 1000

xs = np.linspace(-10, 10, num_steps)
results1A = np.empty(num_steps)   
results1B = np.empty(num_steps)   
results2 = np.empty(num_steps)

for i in range(-1000, 1000):          
    results1A[i] = part1A(i * dt, 0)   
    results1B[i] = part1B(i * dt, 3)
    results2[i] = part2(i * dt, 1, 2)


plt.title("Taylor Series Part 1a")  
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs, results1A)
plt.show()

plt.title("Taylor Series Part 1b")  
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs, results1B)
plt.show()

plt.title("Taylor Series Part 2")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs, results2)
plt.show()