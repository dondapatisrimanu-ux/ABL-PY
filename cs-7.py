def get_performance_category(average):
    if average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Very Good"
    elif average >= 60:
        return "Good"
    elif average >= 40:
        return "Average"
    else:
        return "Needs Improvement"
def get_trend(previous, latest):
    if latest > previous + 1:
        return "Improving"
    elif latest < previous - 1:
        return "Declining"
    else:
        return "Stable"
def main():
    print("=" * 50)
    print("     STUDENT PERFORMANCE TREND ANALYSIS")
    print("=" * 50)
    student_name = input("Enter Student Name: ")
    try:
        subjects = int(input("Enter Number of Subjects: "))
        exams = int(input("Enter Number of Exams (Minimum 2): "))
        if subjects <= 0 or exams < 2:
            print("Invalid input!")
            return
        subject_names = []
        for i in range(subjects):
            subject_names.append(input(f"Enter Subject {i+1} Name: "))

        exam_averages = []
        all_marks = []

        for exam in range(exams):
            print(f"\n--- Exam {exam+1} ---")
            total = 0

            for subject in subject_names:
                while True:
                    try:
                        mark = float(input(f"Enter {subject} Marks (0-100): "))
                        if 0 <= mark <= 100:
                            break
                        else:
                            print("Marks must be between 0 and 100.")
                    except ValueError:
                        print("Enter a valid number.")

                total += mark
                all_marks.append(mark)

            average = total / subjects
            exam_averages.append(average)

        overall_average = sum(all_marks) / len(all_marks)
        category = get_performance_category(overall_average)
        trend = get_trend(exam_averages[-2], exam_averages[-1])

        print("\n" + "=" * 50)
        print("          STUDENT PERFORMANCE REPORT")
        print("=" * 50)
        print(f"Student Name      : {student_name}")

        for i, avg in enumerate(exam_averages, start=1):
            print(f"Exam {i} Average   : {avg:.2f}")

        print("-" * 50)
        print(f"Overall Average   : {overall_average:.2f}")
        print(f"Percentage        : {overall_average:.2f}%")
        print(f"Performance       : {category}")
        print(f"Performance Trend : {trend}")
        print("=" * 50)

    except ValueError:
        print("Invalid input!")


if __name__ == "__main__":
    main()