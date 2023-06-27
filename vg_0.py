import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

k = 20
A = 2
dk = 1
vp = 0.01
vg = 0
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
ax = plt.axes(xlim=(-5, 5), ylim=(-5, 5))
line1, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)
line3, = ax.plot([], [], lw=2)
points, = ax.plot([], [], 'go')
square, = ax.plot([], [], 'rs')

# Ustalenie tego samego koloru dla line2 i line3
line2.set_color('orange')
line3.set_color('orange')

# Ustawienie przezroczystości pomarańczowych linii na 0
line2.set_alpha(0)
line3.set_alpha(0)

def init():
   line1.set_data([], [])
   line2.set_data([], [])
   line3.set_data([], [])
   points.set_data([], [])
   square.set_data([], [])

   return line1, line2, line3, points, square

def animate(i):
   t = i / 308  # Czas

   x = np.linspace(-5, 5, 2000)
   y1 = np.sin(k * (x - vp * i)) * np.cos(dk * (x - vg * i)) * A
   y2 = np.cos(dk * (x - vg * i))*A
   y3 = -np.cos(dk * (x - vg * i))*A

   line1.set_data(x, y1)
   line2.set_data(x, y2)
   line3.set_data(x, y3)

   # Znajdowanie przecięcia y2 i y3
   intersections = np.where(np.diff(np.sign(y2 - y3)))[0]
   x_intersections = x[intersections]
   y_intersections = y2[intersections]

   points.set_data(x_intersections, y_intersections)

   # Aktualizacja pozycji czerwonego kwadratu
   x_square = np.interp(t, np.arange(len(x_intersections)), x_intersections)
   y_square = np.interp(x_square, x, y2)
   square.set_data(x_square, y_square)

   # Dodanie legendy
   ax.legend(['y1', 'Zielone kropki poruszają się z prędkością grupową', 'Czerwony kwadrat porusza się z prędkością fazową'])

   return line1, line2, line3, points, square

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=10000, interval=40, blit=True)
plt.show()
