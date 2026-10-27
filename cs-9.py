def allocate_scholarships(students, budget):
    MIN_SCORE = 70
    MAX_INCOME = 300000
    AWARD_AMOUNT = 10000
    eligible = [
        student for student in students
        if student["score"] >= MIN_SCORE
        and student["income"] <= MAX_INCOME
    ]
    eligible.sort(
        key=lambda student: (
            -student["score"],
            student["income"]
        )
    )
    results = []
    remaining_budget = budget
    for student in eligible:
        if remaining_budget <= 0:
            break
        award = min(AWARD_AMOUNT, remaining_budget)
        results.append({
            "name": student["name"],
            "score": student["score"],
            "income": student["income"],
            "award": award
        })
        remaining_budget -= award
    return results, remaining_budget
def main():
    students = [
        {"name": "Ananya", "score": 92, "income": 180000},
        {"name": "Rahul", "score": 85, "income": 250000},
        {"name": "Meera", "score": 78, "income": 200000},
        {"name": "Arjun", "score": 68, "income": 150000},
        {"name": "Kavya", "score": 88, "income": 350000},
        {"name": "Imran", "score": 74, "income": 280000},
        {"name": "Divya", "score": 81, "income": 220000},
        {"name": "Sanjay", "score": 90, "income": 190000},
        {"name": "Pooja", "score": 73, "income": 290000},
        {"name": "Vikram", "score": 95, "income": 175000},
        {"name": "Nisha", "score": 84, "income": 240000},
        {"name": "Kiran", "score": 76, "income": 270000}
    ]

    budget = 100000

    awards, remaining = allocate_scholarships(
        students, budget
    )

    print("\nUNIVERSITY SCHOLARSHIP ALLOCATION")
    print("-" * 65)
    print(f"{'Student':<12}{'Score':>8}"
          f"{'Family Income':>18}{'Award':>15}")
    print("-" * 65)

    for student in awards:
        print(
            f"{student['name']:<12}"
            f"{student['score']:>7}%"
            f"{student['income']:>18,}"
            f"{student['award']:>15,}"
        )

    total_awarded = sum(
        student["award"] for student in awards
    )

    print("-" * 65)
    print(f"Total awarded: Rs. {total_awarded:,}")
    print(f"Remaining budget: Rs. {remaining:,}")
    print(f"Students awarded: {len(awards)}")


if __name__ == "__main__":
    main()