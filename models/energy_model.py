def calculate_energy(speed_kmph, acceleration, vehicle):
    speed = speed_kmph / 3.6

    rolling_force = vehicle.mass * 9.81 * vehicle.rolling_resistance
    aero_force = 0.5 * vehicle.air_density * vehicle.drag_coeff * vehicle.frontal_area * speed**2
    accel_force = vehicle.mass * acceleration

    traction_power = (rolling_force + aero_force + accel_force) * speed / vehicle.drivetrain_eff

    auxiliary_power = 1500  # 1.5 kW (HVAC, electronics)

    total_power = traction_power + auxiliary_power

    return max(total_power, 0)
