import matplotlib.pyplot as plt

input_values =[1,2,3,4,5]
squares = [1,4,9,16,25]
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)

ax.set_title('Square', fontsize = 24)
ax.set_xlabel('value', fontsize=14)
ax.set_ylabel('value*value', fontsize=14)

ax.tick_params(axis='both', labelsize=14)
plt.show()