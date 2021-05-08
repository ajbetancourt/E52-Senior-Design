import zaxistest as step_motor
#import peak_power_detector as peak_power_detector
import time

class run():
    def __init__(self, increment):
        self.increments = increment
    #    self.plot_points = []
 #       for i in range(0,self.increments+1):
     #       self.plot_points.append(0)

    def motor_data(self):
        for z in range(0,self.increments+1):
      #      self.plot_points.append(peak_power_detector.main())
            step_motor.move_up()
            time.sleep(0.5) ##might not need this, but this will pause just in case the plot_points function drags
            #z axis only have file for multiple axis 3 for loop-- was sent to tyler if lost.
        for z in range(0, self.increments):
            step_motor.move_down()
        
        
    def getPlot(self):
        return self.plot_points

    def getInc(self):
        return self.increments
