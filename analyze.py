import numpy
import matplotlib.pyplot

'''
backLegSensorValue = numpy.load('data/backLegSensorValue.npy')
frontLegSensorValue = numpy.load('data/frontLegSensorValue.npy')
matplotlib.pyplot.plot(backLegSensorValue, label='backLegSensorValue')
matplotlib.pyplot.plot(frontLegSensorValue, label='frontLegSensorValue', linewidth=3)
'''

targetAnglesBackLeg = numpy.load('data/targetAnglesBackLeg.npy')
targetAnglesFrontLeg = numpy.load('data/targetAnglesFrontLeg.npy')
matplotlib.pyplot.plot(targetAnglesBackLeg, label='targetAnglesBackLeg')
matplotlib.pyplot.plot(targetAnglesFrontLeg, label='targetAnglesFrontLeg')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
# print(backLegSensorValue)