def simulate_water_tank(capacity, initial_level, days,
                        daily_inflow, daily_demand):
    if capacity <= 0:
        raise ValueError("Capacity must be greater than zero.")
    if not 0 <= initial_level <= capacity:
        raise ValueError("Initial level must be within tank capacity.")
    if days <= 0:
        raise ValueError("Number of days must be positive.")
    if daily_inflow < 0 or daily_demand < 0:
        raise ValueError("Inflow and demand cannot be negative.")
    level = initial_level
    print("\nMULTI-DAY WATER TANK SIMULATION")
    print("-" * 75)
    print("Day | Opening | Inflow | Supplied | Overflow | Unmet | Closing | Status")
    print("-" * 75)
    for day in range(1, days + 1):
        opening = level
        available = opening + daily_inflow
        overflow = max(available - capacity, 0)
        available = min(available, capacity)
        supplied = min(daily_demand, available)
        unmet = daily_demand - supplied
        level = available - supplied
        status = "LOW WATER" if level <= capacity * 0.20 else "OK"
        print(
            f"{day:3} | {opening:7.1f} | {daily_inflow:6.1f} | "
            f"{supplied:8.1f} | {overflow:8.1f} | {unmet:5.1f} | "
            f"{level:7.1f} | {status}"
        )
    print("-" * 75)
    print(f"Final water level: {level:.1f} liters")


def main():
    print("MULTI-DAY WATER TANK SIMULATION")

    try:
        capacity = float(input("Enter tank capacity (liters): "))
        initial = float(input("Enter initial water level (liters): "))
        days = int(input("Enter number of days: "))
        inflow = float(input("Enter daily inflow (liters): "))
        demand = float(input("Enter daily water demand (liters): "))

        simulate_water_tank(
            capacity, initial, days, inflow, demand
        )

    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()