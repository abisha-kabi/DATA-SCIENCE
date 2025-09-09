import matplotlib.pyplot as plt
temp = [12, 14, 16, 18, 20, 22, 24]
celsius = [100, 200, 250, 400, 300, 450, 500]
plt.figure(figsize=(8, 6))
plt.plot(temp, celsius, marker='o', linestyle='--', color='black', label='Celsius vs Temp')
plt.xlabel("Temperature")
plt.ylabel("Celsius")
plt.title("Temperature vs Celsius")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()