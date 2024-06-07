from statistics import mean

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
academic_performance = dict()
for i in range(len(grades)):
    academic_performance[students[i]] = mean(grades[i])
print(academic_performance)
