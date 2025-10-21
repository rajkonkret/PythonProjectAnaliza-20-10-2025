from matplotlib import pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 9]

plt.plot(x,y, c="green")
plt.title("Wykres liniowy")
plt.xlabel("Oś X")
plt.ylabel("Oś Y")

plt.show()