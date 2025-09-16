import matplotlib.pyplot as plt
import numpy as np
groups = ['A', 'B', 'C', 'D', 'E']
men_scores = [22, 30, 35, 35, 36]
women_scores = [25, 32, 30, 35, 29]
bar_width = 0.35
r1 = np.arange(len(groups))
r2 = [x + bar_width for x in r1]
plt.bar(r1, men_scores, color='blue', width=bar_width, edgecolor='black', label='Men')
plt.bar(r2, women_scores, color='pink', width=bar_width, edgecolor='black', label='Women')
plt.xticks([r + bar_width/2 for r in range(len(groups))], groups)
plt.show()
