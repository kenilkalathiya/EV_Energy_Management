class Battery:
    def __init__(self, capacity_kwh=60):
        self.capacity = capacity_kwh          # kWh
        self.soc = 0.8                         # 80% initial SOC

    def consume_energy(self, energy_kwh):
        self.soc -= energy_kwh / self.capacity
        self.soc = max(self.soc, 0)

    def get_soc_percent(self):
        return round(self.soc * 100, 2)
