import numpy

rangeValue = 10000
amplitudeBackLeg = numpy.pi/4.0
frequencyBackLeg = 10
phaseOffsetBackLeg = numpy.pi
amplitudeFrontLeg = numpy.pi/4.0
frequencyFrontLeg = 10
phaseOffsetFrontLeg = 0
amplitudeBackArm = numpy.pi/4.0
frequencyBackArm = 10
phaseOffsetBackArm = numpy.pi
amplitudeFrontArm = numpy.pi/4.0
frequencyFrontArm = 10
phaseOffsetFrontArm = 0
amplitudeLeftLeg = numpy.pi/4.0
frequencyLeftLeg = 10
phaseOffsetLeftLeg = 0
amplitudeRightLeg = numpy.pi/4.0
frequencyRightLeg = 10
phaseOffsetRightLeg = 0
amplitudeLeftArm = numpy.pi/4.0
frequencyLeftArm = 10
phaseOffsetLeftArm = 0
amplitudeRightArm = numpy.pi/4.0
frequencyRightArm = 10
phaseOffsetRightArm = 0
backLegSensorValue = numpy.zeros(rangeValue)
frontLegSensorValue = numpy.zeros(rangeValue)
backArmSensorValue = numpy.zeros(rangeValue)
frontArmSensorValue = numpy.zeros(rangeValue)
leftLegSensorValue = numpy.zeros(rangeValue)
frontLegSensorValue = numpy.zeros(rangeValue)
leftArmSensorValue = numpy.zeros(rangeValue)
rightArmSensorValue = numpy.zeros(rangeValue)

# targetAngles = numpy.sin(numpy.linspace(0, 2.0*numpy.pi, rangeValue))
# targetAngles = ((-targetAngles + 1) / 2.0) * (numpy.pi / 2.0) - (numpy.pi / 4.0)
targetAnglesBackLeg = amplitudeBackLeg*numpy.sin(frequencyBackLeg*numpy.linspace(0, 2.0*numpy.pi, rangeValue) + phaseOffsetBackLeg)
targetAnglesFrontLeg = amplitudeFrontLeg*numpy.sin(frequencyFrontLeg*numpy.linspace(0, 2.0*numpy.pi, rangeValue) + phaseOffsetFrontLeg)
targetAnglesBackArm = amplitudeBackArm*numpy.sin(frequencyBackArm*numpy.linspace(0, 2.0*numpy.pi, rangeValue) + phaseOffsetBackArm)
targetAnglesFrontArm = amplitudeFrontArm*numpy.sin(frequencyFrontArm*numpy.linspace(0, 2.0*numpy.pi, rangeValue) + phaseOffsetFrontArm)
targetAnglesLeftLeg = amplitudeLeftLeg*numpy.sin(frequencyLeftLeg*numpy.linspace(0, 2.0*numpy.pi, rangeValue) + phaseOffsetLeftLeg)
targetAnglesRightLeg = amplitudeRightLeg*numpy.sin(frequencyRightLeg*numpy.linspace(0, 2.0*numpy.pi, rangeValue) + phaseOffsetRightLeg)
targetAnglesLeftArm = amplitudeLeftArm*numpy.sin(frequencyLeftArm*numpy.linspace(0, 2.0*numpy.pi, rangeValue) + phaseOffsetLeftArm)
targetAnglesRightArm = amplitudeRightArm*numpy.sin(frequencyRightArm*numpy.linspace(0, 2.0*numpy.pi, rangeValue) + phaseOffsetRightArm)
# numpy.save('data/targetAnglesBackLeg.npy', numpy.array(targetAnglesBackLeg))
# numpy.save('data/targetAnglesFrontLeg.npy', numpy.array(targetAnglesFrontLeg))

numberOfGenerations = 10
populationSize = 6

numSensorNeurons = 9
numMotorNeurons = 8

motorJointRange = 0.35