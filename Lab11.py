import os
import matplotlib.pyplot as plt
if __name__=='__main__':
        submission_folder="data/submissions"
        student_file = open("data/students.txt", "r")
        student_content = student_file.readlines()
        assignments_file = open("data/assignments.txt", "r")
        assignments_content=assignments_file.readlines()
        print("1. Student grade")
        print("2. Assignment statistics")
        print("3. Assignment graph")
        print()
        selection=int(input("Enter your selection:"))
        if selection==1:
            student_name=input("What is the student's name: ")
            for line in student_content:
                if line[3:].strip()==student_name:
                    student_id=line[:3].strip()
                    student_total_points=0
                    grade_count=0
                    for file in os.listdir(submission_folder):
                        file_path=os.path.join(submission_folder,file)
                        individual_submission=open(file_path,"r")
                        individual_submission_content=individual_submission.readlines()
                        if individual_submission_content[0][:3].strip()==student_id:
                            submission_splits=individual_submission_content[0].strip().split("|")
                            student_assignment_grade=int(submission_splits[2])
                            assignment_code=submission_splits[1]
                            for i in range(len(assignments_content)):
                                if assignments_content[i].strip()==assignment_code:
                                    if i+1<len(assignments_content):
                                        assignment_weight=int(assignments_content[i+1].strip())
                                        student_assignment_grade*=assignment_weight
                                        student_total_points+=student_assignment_grade
                                        grade_count+=1
                    print(f"{student_total_points//1000}%")
                    print()
            if not student_total_points:
                print("Student not found")
        if selection==2:
            assignments_name=input("What is the assignment name: ")
            assignment_list=[]
            for i in range(len(assignments_content)):
                if assignments_content[i].strip()==assignments_name:
                    assignment_code=assignments_content[i+1].strip()
                    for file in os.listdir(submission_folder):
                        file_path=os.path.join(submission_folder,file)
                        individual_submission=open(file_path,"r")
                        individual_submission_content=individual_submission.readlines()
                        submission_splits = individual_submission_content[0].strip().split("|")
                        student_assignment_code = int(submission_splits[1])
                        if student_assignment_code==int(assignment_code):
                            assignment_list.append(int(submission_splits[2]))
            if assignment_list==[]:
                print("Assignment not found")
            else:
                average_grade=round(sum(assignment_list)//len(assignment_list),2)
                print(f"Min: {min(assignment_list)}%")
                print(f"Avg: {average_grade}%")
                print(f"Max: {max(assignment_list)}%")
        if selection==3:
            assignments_name = input("What is the assignment name: ")
            assignment_list = []
            for i in range(len(assignments_content)):
                if assignments_content[i].strip() == assignments_name:
                    assignment_code = assignments_content[i + 1].strip()
                    for file in os.listdir(submission_folder):
                        file_path = os.path.join(submission_folder, file)
                        individual_submission = open(file_path, "r")
                        individual_submission_content = individual_submission.readlines()
                        submission_splits = individual_submission_content[0].strip().split("|")
                        student_assignment_code = int(submission_splits[1])
                        if student_assignment_code == int(assignment_code):
                            assignment_list.append(int(submission_splits[2]))
            if assignment_list==[]:
                print("Assignment not found")
            else:
                bins=[i for i in range((min(assignment_list)-(min(assignment_list)%5)),101,5)]
                plt.hist(assignment_list, bins=bins)
                plt.show()












