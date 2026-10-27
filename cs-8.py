VIOLATIONS = {
    1: ("Overspeeding", 1000),
    2: ("Riding without a helmet", 500),
    3: ("Driving without a seat belt", 500),
    4: ("Traffic signal violation", 1000),
    5: ("Illegal parking", 500),
    6: ("Using a mobile phone while driving", 1500)
}
REPEAT_MULTIPLIER = 1.5
def calculate_penalty(selected, offence_count):
    if not selected:
        raise ValueError("Select at least one violation.")
    if any(choice not in VIOLATIONS for choice in selected):
        raise ValueError("Invalid violation selection.")
    if offence_count < 1:
        raise ValueError("Offence count must be at least 1.")
    subtotal = sum(VIOLATIONS[i][1] for i in selected)
    multiplier = (
        REPEAT_MULTIPLIER if offence_count > 1 else 1.0
    )
    total = subtotal * multiplier
    return subtotal, multiplier, total
def main():
    print("=" * 55)
    print("       TRAFFIC VIOLATION PENALTY CALCULATOR")
    print("=" * 55)
    print("Example penalties only; verify applicable local laws.\n")
    for number, (name, amount) in VIOLATIONS.items():
        print(f"{number}. {name} - Rs. {amount}")
    try:
        choices = input(
            "\nEnter violation numbers separated by commas: "
        )
        selected = [
            int(item.strip())
            for item in choices.split(",")
            if item.strip()
        ]

        offence_count = int(
            input("Enter offence count (1 for first offence): ")
        )

        subtotal, multiplier, total = calculate_penalty(
            selected, offence_count
        )

        print("\n========== PENALTY REPORT ==========")

        for choice in selected:
            name, amount = VIOLATIONS[choice]
            print(f"{name:<35} Rs. {amount:.2f}")

        print("------------------------------------")
        print(f"Subtotal:              Rs. {subtotal:.2f}")

        if multiplier > 1:
            print(f"Example multiplier:    x{multiplier:.1f}")

        print(f"TOTAL PENALTY:         Rs. {total:.2f}")
        print("====================================")

    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()