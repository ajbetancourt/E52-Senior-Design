from zaxistest.py import zaxistest as motor
from peak_power_detector.py import peak_power

increment = 5
def motor_data(increment):
    plot_points = []
    for z in range(0,increment):
        step_motor()
        peak_power_de

if __name__ =='__main__':
    motor_data()