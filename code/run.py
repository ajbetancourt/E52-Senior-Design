import zaxistest as step_motor
import peak_power_detector as peak_power_detector


plot_points = [0]*increment
def motor_data(increment):
    plot_points = []
    for i in range(0,increment+1):
        buckets.append(0)
    for z in range(0,increment+1):
        step_motor.move_up()
        plot_points.append(peak_power_detector.main())
        #time.sleep(0.25) ##might not need this, but this will pause just in case the plot_points function drags
        #z axis only have file for multiple axis 3 for loop-- was sent to tyler if lost.
    for z in range(0, increment+1):
        step_motor.move_down()
    return plot_points, increment

