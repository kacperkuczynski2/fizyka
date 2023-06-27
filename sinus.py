import numpy
import matplotlib.pyplot as plot
import matplotlib.animation as animation

figure = plot.figure()
plot.xlim(0, 2*numpy.pi), plot.ylim(-4, 4)
line, = plot.plot([])

def animate(i):
    x = numpy.arange(0, 2*numpy.pi, 0.001)
    y = numpy.sin(2*numpy.pi * (x - 0.01*i))
    # y = sin(10 * 2pi * x)
    line.set_data(x, y)
    return line,

wave = animation.FuncAnimation(figure, animate, frames = 1000,
                               interval = 10, blit = True)

plot.show()