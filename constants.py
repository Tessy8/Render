import numpy

rangeValue = 1000
amplitudeBackLeg = numpy.pi/4.0
frequencyBackLeg = 10
phaseOffsetBackLeg = numpy.pi
amplitudeFrontLeg = numpy.pi/4.0
frequencyFrontLeg = 50
phaseOffsetFrontLeg = 0
backLegSensorValue = numpy.zeros(rangeValue)
frontLegSensorValue = numpy.zeros(rangeValue)

# targetAngles = numpy.sin(numpy.linspace(0, 2.0*numpy.pi, rangeValue))
# targetAngles = ((-targetAngles + 1) / 2.0) * (numpy.pi / 2.0) - (numpy.pi / 4.0)
targetAnglesBackLeg = amplitudeBackLeg*numpy.sin(frequencyBackLeg*numpy.linspace(0, 2.0*numpy.pi, rangeValue) + phaseOffsetBackLeg)
targetAnglesFrontLeg = amplitudeFrontLeg*numpy.sin(frequencyFrontLeg*numpy.linspace(0, 2.0*numpy.pi, rangeValue) + phaseOffsetFrontLeg)
# numpy.save('data/targetAnglesBackLeg.npy', numpy.array(targetAnglesBackLeg))
# numpy.save('data/targetAnglesFrontLeg.npy', numpy.array(targetAnglesFrontLeg))

numberOfGenerations = 10
populationSize = 10