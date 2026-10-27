def decide_admission(name, academic_percentage, entrance_score):
    MIN_ACADEMIC_PERCENTAGE = 60
    MIN_ENTRANCE_SCORE = 50
    if not 0 <= academic_percentage <= 100:
        return "Invalid academic percentage!"
    if not 0 <= entrance_score <= 100:
        return "Invalid entrance exam score!"
    if (academic_percentage >= MIN_ACADEMIC_PERCENTAGE
            and entrance_score >= MIN_ENTRANCE_SCORE):
        decision = "Eligible for Admission"
        reason = "All eligibility criteria are satisfied."
    else:
        decision = "Not Eligible for Admission"
        reason = "Minimum admission criteria are not satisfied."
    print("\n--- Admission Decision Report ---")
    print("Student Name:", name)
    print("Academic Percentage:", academic_percentage, "%")
    print("Entrance Exam Score:", entrance_score, "/100")
    print("Decision:", decision)
    print("Reason:", reason)
    return decision
def main():
    print("UNIVERSITY ADMISSION DECISION ENGINE")
    print("------------------------------------")
    name = input("Enter student name: ").strip()
    if not name:
        print("Error: Student name cannot be empty.")
        return
    try:
        academic_percentage = float(
            input("Enter academic percentage (0-100): ")
        )
        entrance_score = float(
            input("Enter entrance exam score (0-100): ")
        )

        decide_admission(
            name,
            academic_percentage,
            entrance_score
        )

    except ValueError:
        print("Error: Please enter valid numeric scores.")


if __name__ == "__main__":
    main()