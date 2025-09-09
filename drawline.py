import matplotlib.pyplot as plt
x = [1, 2, 6, 18]
y = [3, 10, 12, 20]
plt.figure(figsize=(8, 6))
plt.plot(x, y, linestyle=':', color='blue', label='Path')
plt.scatter(x, y, color='red', zorder=5)
for i in range(len(x)):
    plt.text(x[i]+0.5, y[i], f'({x[i]}, {y[i]})', fontsize=9, color='red')
plt.title("Dotted Line with Red Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()