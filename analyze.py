import numpy
import matplotlib.pyplot

backLegSensorValue = numpy.load('data/backLegSensorValue.npy')
frontLegSensorValue = numpy.load('data/frontLegSensorValue.npy')
matplotlib.pyplot.plot(backLegSensorValue, label='backLegSensorValue')
matplotlib.pyplot.plot(frontLegSensorValue, label='frontLegSensorValue', linewidth=3)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
# print(backLegSensorValue)