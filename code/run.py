import zaxistest as step_motor
import peak_power_detector as peak_power_detector

increment = 5
def motor_data(increment):
    plot_points = []
    for z in range(0,increment):
        step_motor.main()
        plot_points[z] = peak_power_detector.main()
        #z axis only have file for multiple axis 3 for loop-- was sent to tyler if lost.

    return plot_points