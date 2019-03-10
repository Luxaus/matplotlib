"""
===========
FrameImagesFileMovieWriter
===========

This example uses a FrameImagesFileMovieWriter to grab each frame and store into a directory.

"""
# -*- noplot -*-

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

fig = plt.figure()
l, = plt.plot([], [], 'k-o')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

x0, y0 = 0, 0

HTMLWriter = manimation.writers['frameimages']
writer = HTMLWriter(fps=15)

with writer.saving(fig, "writer_test.svg", 10):
    for i in range(10):
        x0 += 1
        l.set_data(x0, y0)
        writer.grab_frame()
