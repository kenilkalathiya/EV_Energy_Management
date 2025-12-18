from models.vehicle_model import VehicleModel
from models.energy_model import calculate_energy
from models.battery_model import Battery
from control.eco_mode import eco_mode_decision
from data.driving_profiles import CITY_PROFILE

TIME_STEP_SEC = 1500  # each step = 5 seconds


vehicle = VehicleModel()
battery = Battery()
acceleration = 0.4  # m/s^2

print("Step | Speed | SOC (%) | Eco Decisions")
print("-" * 60)

for step, speed in enumerate(CITY_PROFILE):
    power = calculate_energy(speed, acceleration, vehicle)
    energy_kwh = (power * TIME_STEP_SEC) / 3600000  # W → kWh per step

    battery.consume_energy(energy_kwh)
    soc = battery.get_soc_percent()
    actions = eco_mode_decision(soc)

    print(f"{step:>4} | {speed:>5} | {soc:>7} | {', '.join(actions)}")
