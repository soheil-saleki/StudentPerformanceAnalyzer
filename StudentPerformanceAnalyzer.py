"""Hi 
Name : Soheil Saleki
This is gonna be a full report of a class performance
What does it do?
-Calculates average of each student
-Calculates the average of the class
-Find the best and weakest student in the class
-Pass/Fail system
"""


import os
def main():
    students = {}
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "student.txt")
    with open(file_path , "r") as file:
        for line in file:
            line = line.strip()
            parts = line.split(",")
            name = parts[0]
            math_score = int(parts[1])
            python_score = int(parts[2])
            sql_score = int(parts[3])
            students[name] = {
                "math" : math_score,
                "python" : python_score,
                "sql" : sql_score
            }
    return students
def calculate_average(scores: list[int]) -> float:
    total = 0 
    count = 0 
    for score in scores:
        total += score
        count += 1
    return total / count

def passes_fails(data: dict[str,dict[str,int]])->list[str,float,str]:
    result = {}
    for student, subject_dict in data.items():
        avg = calculate_average(subject_dict.values())
        if avg >= 65:
            result[student] = "Pass"
        else :
            result[student] ="Fail"
    return result

def class_avg(data: dict[str,dict[str,int]])-> float:
    total = 0
    count = 0
    for student, subject_dict in data.items():
        scores = list(subject_dict.values())
        total += calculate_average(scores)
        count += 1
    return total / count

def top_student(data: dict[str,dict[str,int]])->tuple[float,str]:
    highest = 0
    top_name = ""
    for student, subject_dict in data.items():
        avg = calculate_average(subject_dict.values())
        if highest < avg:
            highest = avg
            top_name = student
    return highest , top_name

def weakest_student(data: dict[str,dict[str,int]]) -> tuple[float,str]:
    lowest = float("inf")
    weakest_name = ""
    for student, subject_dict in data.items():
        avg = calculate_average(subject_dict.values())
        if lowest > avg:
            lowest = avg
            weakest_name = student
    return lowest , weakest_name

"""report"""
def print_report(data: dict[str,dict[str,int]]) ->None:
    highest , top_name = top_student(data)
    lowest , weakest_name = weakest_student(data)
    result = passes_fails(data)
    print("----Class Report----")
    print(f"Class Average: {class_avg(data):.2f}")
    print("-"*30)
    print(f"Top Student: {top_name}-{highest:.2f}")
    print(f"Weakest Student: {weakest_name}-{lowest:.2f}")
    print("\n----Student Status----")
    print(f"{'Student':>7} {'Average':>10} {'Status':>10}")
    print("-"*30)
    for student, subjects in sorted(data.items() , key=lambda x: calculate_average(x[1].values()) , reverse=True):
        avg = calculate_average(subjects.values())
        print(f"{student} - {avg:>10.2f} - {result[student]:>10}")
if __name__ == "__main__":
    students = main()
    print_report(students)
    

