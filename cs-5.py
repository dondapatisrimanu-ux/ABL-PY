import math
PARKING_RATES = {
    "bike": 20,
    "car": 50,
    "bus": 100
}
def calculate_parking_fee(vehicle_type, duration):
    vehicle = vehicle_type.strip().lower()
    if vehicle not in PARKING_RATES:
        raise ValueError("Invalid vehicle type. Choose Bike, Car, or Bus.")
    try:
        hours = float(duration)
    except (TypeError, ValueError):
        raise ValueError("Duration must be a valid number.")
    if not math.isfinite(hours) or hours <= 0:
        raise ValueError("Parking duration must be greater than zero.")
    billable_hours = math.ceil(hours)
    rate = PARKING_RATES[vehicle]
    total_fee = billable_hours * rate
    return vehicle.title(), hours, billable_hours, rate, total_fee
def main():
    print("=" * 40)
    print(" SMART PARKING FEE MANAGEMENT SYSTEM")
    print("=" * 40)
    print("\nVehicle types and hourly rates:")
    print("Bike : Rs. 20 per hour")
    print("Car  : Rs. 50 per hour")
    print("Bus  : Rs. 100 per hour")
    vehicle_type = input("\nEnter vehicle type: ")
    duration = input("Enter parking duration in hours: ")
    try:
        vehicle, hours, billable_hours, rate, fee = (
            calculate_parking_fee(vehicle_type, duration)
        )

        print("\n" + "=" * 40)
        print("          PARKING FEE RECEIPT")
        print("=" * 40)
        print(f"Vehicle Type     : {vehicle}")
        print(f"Parking Duration : {hours:g} hours")
        print(f"Billable Hours   : {billable_hours}")
        print(f"Rate Per Hour    : Rs. {rate}")
        print("-" * 40)
        print(f"Total Parking Fee: Rs. {fee:.2f}")
        print("=" * 40)

    except ValueError as error:
        print("\nError:", error)


if __name__ == "__main__":
    main()