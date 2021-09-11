if __name__ == '__main__':
    students_grade = [["Mike", 60], ["Joe", 75], ["Sue", 85], ["Ann", 80], ["George", 75]]

    sorted_scores = sorted(list(set([x[1] for x in students_grade])))

    second_lowest = sorted_scores[1]

    print("Second lowest score is", second_lowest)
    print()

    low_final = []
    for student in students_grade:

        if second_lowest == student[1]:
            low_final.append(student[0])
    for student in sorted(low_final):
        print(student, "had a score of ", second_lowest)
