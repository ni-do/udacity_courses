from matplotlib import pyplot
from numpy import arange
import bisect

labels = ['traktoren', 'maehdrescher', 'grubber']
data = [528, 322,182]

pos=arange(len(data))
pyplot.xticks(pos+0.4,labels)
pyplot.bar(pos,data)
pyplot.show()