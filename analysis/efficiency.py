def calculate_efficiency(total_energy_wh, total_distance_km):
    if total_distance_km == 0:
        return 0
    return round(total_energy_wh / total_distance_km, 2)
