import numpy as np
import pandas as pd

class RocketSimulator:
    def __init__(self, dry_mass=100.0, fuel_mass=50.0, thrust=5000.0, burn_time=10.0, dt=0.1):
        """
        Initialize rocket parameters.
        dry_mass: Mass of the rocket without fuel (kg)
        fuel_mass: Mass of the fuel (kg)
        thrust: Engine thrust (N)
        burn_time: Time until fuel is exhausted (s)
        dt: Time step for simulation (s)
        """
        self.dry_mass = dry_mass
        self.fuel_mass = fuel_mass
        self.thrust = thrust
        self.burn_time = burn_time
        self.dt = dt
        self.g = 9.81  # Gravity (m/s^2)
        self.drag_coefficient = 0.5 # Simplified drag
        self.air_density = 1.225 # Sea level (kg/m^3)
        self.cross_section_area = 0.1 # m^2

    def run(self):
        """
        Runs the simulation using Euler integration.
        Returns a DataFrame with time-series data.
        """
        t = 0.0
        h = 0.0 # Height
        v = 0.0 # Velocity
        current_fuel = self.fuel_mass
        
        results = []
        
        # Simulate until it hits the ground (h < 0) or a max time limit
        while (h >= 0 or t == 0) and t < 300:
            # 1. Determine Mass
            total_mass = self.dry_mass + current_fuel
            
            # 2. Determine Forces
            # Thrust: Only if fuel remains & t < burn_time
            if t < self.burn_time and current_fuel > 0:
                F_thrust = self.thrust
                # Burn fuel linearly
                fuel_rate = self.fuel_mass / self.burn_time
                current_fuel -= fuel_rate * self.dt
                if current_fuel < 0: current_fuel = 0
            else:
                F_thrust = 0.0
                
            # Gravity
            F_gravity = total_mass * self.g
            
            # Drag: F = 0.5 * rho * v^2 * Cd * A
            # Direction is opposite to velocity
            drag_sign = 1 if v > 0 else -1
            F_drag = 0.5 * self.air_density * (v**2) * self.drag_coefficient * self.cross_section_area * drag_sign
            
            # Net Force
            F_net = F_thrust - F_gravity - F_drag
            
            # 3. Kinematics (Newton's 2nd Law)
            # a = F / m
            a = F_net / total_mass
            
            # Update State (Euler Integration)
            v += a * self.dt
            h += v * self.dt
            t += self.dt
            
            results.append({
                "Time (s)": t,
                "Altitude (m)": h,
                "Velocity (m/s)": v,
                "Acceleration (m/s^2)": a,
                "Thrust (N)": F_thrust,
                "Mass (kg)": total_mass
            })
            
            # Stop if we hit the ground with negative velocity (falling)
            if h < 0 and v < 0:
                h = 0
                break
                
        return pd.DataFrame(results)
