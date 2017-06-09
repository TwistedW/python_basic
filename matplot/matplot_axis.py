import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = x**2
y2 = x*3+1

plt.figure(num=1)
l1, = plt.plot(x, y2, label='liner')
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='square')

plt.xlim(-4, 3)
plt.ylim(-1, 10)
plt.xlabel('X axis')
plt.ylabel('Y axis')
new_ticks = np.linspace(-4, 3, 15)
plt.xticks(new_ticks)
plt.yticks([-1, 0, 1.3, 8], [r'$really\ bad$', r'$bad$', r'$good$', r'$really\ good$'])
# to use '$ $' for math text and nice looking, e.g. '$\pi$'

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')# ACCEPTS: [ 'top' | 'bottom' | 'both' | 'default' | 'none' ]
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))# data: depend on y data
ax.spines['left'].set_position(('data', 0))

plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='upper left')
"""legend( handles=(line1, line2, line3),
           labels=('label1', 'label2', 'label3'),
           'upper right')
    The *loc* location codes are::
          'best' : 0,          (currently not supported for figure legends)
          'upper right'  : 1,
          'upper left'   : 2,
          'lower left'   : 3,
          'lower right'  : 4,
          'right'        : 5,
          'center left'  : 6,
          'center right' : 7,
          'lower center' : 8,
          'upper center' : 9,
          'center'       : 10,"""

plt.show()