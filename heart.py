import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.sqrt(6), np.sqrt(6), 400)   


y_upper = np.sqrt(6 - x**2) + np.abs(x)  # Upper part of the heart
y_lower = -np.sqrt(6 - x**2) + np.abs(x)  # Lower part of the heart

plt.plot(x, y_upper, 'r')  # Plot upper curve in red
plt.plot(x, y_lower, 'b')  # Plot lower curve in blue

# Plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Heart Function Outline')
plt.axhline(0, color='black', linewidth=0.5)  
plt.axvline(0, color='black', linewidth=0.5)  
plt.grid(True, linestyle='--', alpha=0.5)  
plt.show() 
