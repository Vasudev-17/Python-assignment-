# Function to calculate grade based on average score
def calculate_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'

# Main program
def main():
    # Ask for the student's name
    student_name = input("Enter the student's name: ")

    # Ask for the number of subjects
    num_subjects = int(input("Enter the number of subjects: "))

    # Initialize total score
    total_score = 0

    # Input scores for each subject
    for i in range(num_subjects):
        score = float(input(f"Enter the score for subject {i+1}: "))
        total_score += score

    # Calculate the average score
    average_score = total_score / num_subjects

    # Determine the grade based on the average score
    grade = calculate_grade(average_score)

    # Display the results
    print(f"\nStudent: {student_name}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Grade: {grade}")

# Run the program
if __name__ == "__main__":
    main()
  
