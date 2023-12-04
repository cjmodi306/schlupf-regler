import numpy as np

class Wheel:
    def __init__(self, tyre_diameter):
        self.tyre_diameter = tyre_diameter #tyre_diameter in meter
    
    def get_wheel_velocity(self, angular_velocity):
        return np.pi*self.tyre_diameter*angular_velocity
    
    def get_slip(self, vehicle_velocity):
        v_a = self.get_wheel_velocity(200)
        return (vehicle_velocity-v_a)/vehicle_velocity
    

FrontRightWheel = Wheel(tyre_diameter=0.5)
FrontLeftWheel  = Wheel(tyre_diameter=0.5)
RearRightWheel  = Wheel(tyre_diameter=0.5)
RearRightWheel  = Wheel(tyre_diameter=0.5)


print(FrontLeftWheel.get_wheel_velocity(angular_velocity=100))
