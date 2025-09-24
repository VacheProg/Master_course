# dictionary
students = {
    'Armen': {'ruseren': 10, 'angleren': 7, 'hayoc lezu': 9},
    'Hayk': {'ruseren': 7, 'angleren': 6, 'hayoc lezu': 5}
}
for name, subjects in students.items():
    avg = sum(subjects.values()) / len(subjects)
    print(name, "=", avg)

subjects_avg = {}
for name, subjects in students.items():
    for subject, grade in subjects.items():
        if subject not in subjects_avg:
            subjects_avg[subject] = []
        subjects_avg[subject].append(grade)
for subject, grades in subjects_avg.items():
    avg1 = sum(grades) / len(grades)
    print(subject, '=', avg1)