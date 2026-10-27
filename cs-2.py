def calculate_water_bill(units):
    if units < 0:
        raise ValueError("Water consumption cannot be negative.")
    bill = 0
    slab1 = min(units, 10)
    bill += slab1 * 5
    slab2 = min(max(units - 10, 0), 10)
    bill += slab2 * 8
    slab3 = min(max(units - 20, 0), 20)
    bill += slab3 * 12
    slab4 = max(units - 40, 0)
    bill += slab4 * 15
    return bill
def main():
    print("PROGRESSIVE WATER TARIFF ANALYSIS")
    print("---------------------------------")
    try:
        units = float(input("Enter water consumption in units: "))

        if units < 0:
            print("Error: Consumption cannot be negative.")
            return

        bill = calculate_water_bill(units)

        print("\nWATER BILL DETAILS")
        print(f"Water consumption : {units:g} units")
        print(f"Total water bill  : ₹{bill:.2f}")

    except ValueError:
        print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()