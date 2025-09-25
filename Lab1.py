import sys
import os
import heapq
def show_students_by_lastname_dict(lastname, option):
        lastname = lastname.lower()

        if lastname not in dict_lastname:
            print()
            return
        
        for student in dict_lastname[lastname]:
        
            print("Student Last Name:", student[0])
            print("Student First Name:",student[1])
            if option == "b":
                print("Taken BusRoute:", student[4])
            else:
                print("Student ClassRoom:", student[3])
                print("Teacher LastName:", student[6])
                print("Teacher FirstName:", student[7])

def print_teachers_students(Tlastname):
    if Tlastname not in dict_teacher:
        print()
        return
    
    print("Showing students of teacher:", Tlastname)
    List_of_students = dict_teacher[Tlastname]
    for student in List_of_students:
        print("Student:",student)
    return

def print_by_grade(grade):
    if grade not in dict_grade:
        print()
        return
    print("Shwoing Students in grade:", grade)
    list_of_students = dict_grade[grade]
    for student in list_of_students:
        print("Last: " + student[0] + " First:" + student[1])
    return

def print_by_bus_route(bus):
    if bus not in dict_buses:
        print()
        return
    print("Showing Students by bus route: ")
    list_of_students = dict_buses[bus]
    for student in list_of_students:
        print("Student: ", student)
    return

def print_high_low_gpa(grade, high_low):
    if grade not in dict_grade:
        print()
        return

    if high_low.lower() == "low":
        print("Student with lowest gpa in grade:", grade)
        c_s = min(dict_grade[grade], key=lambda s: float(s[5]))
    else:
        print("Student with highest gpa in grade:", grade)
        c_s = max(dict_grade[grade], key=lambda s: float(s[5]))


    print("Student: " + c_s[0] + " " + c_s[1] + " " + c_s[4] + " " + c_s[5] + " " + c_s[6] + " " + c_s[7])
    return

def compute_avg_gpa_for_grade(grade):
    total = 0
    curr_grade = dict_grade[grade]
    for s in curr_grade:
        total += float(s[5])
    print("Average gpa of grade:", grade)
    avg = total/len(curr_grade)
    print(round(avg, 2))
    return


dict_lastname = {}
dict_teacher = {}
dict_grade = {}
dict_buses = {}

with open("students.txt", "r") as file:
    if not os.path.isfile("students.txt"):
        print("Error: file not found")
        sys.exit(1)

    for line in file:
    
        #split the words by ","
        words = line.strip().split(",")
        
        if len(words) != 8:
            print("Incorrect format in file")
            sys.exit(1)

        # add last names to a dictionary
        #only last names

        # I COULD MAKE A LIST OF [words] IF THERE ARE MULTIPLE PEOPLE WITH THE LAST NAME
        key_lastname = words[0].lower()
        if key_lastname not in dict_lastname:
            dict_lastname[key_lastname] = [words]
        else:
            dict_lastname[key_lastname].append(words)

        # make a dictionary of the teachers name, and whenever we run into that teachers name append the student to the list
        if words[6].lower() not in dict_teacher:
            dict_teacher[words[6].lower()] = [words[0] + " " + words[1]]
        else:
            dict_teacher[words[6].lower()].append(words[0] + " " + words[1])

        # make a dictionary of the grades and put each student in the respective grade i = 2
        if words[2] not in dict_grade:
            dict_grade[words[2]] = [words]
        else:
            dict_grade[words[2]].append(words)

        # make dictionary of buses
        if words[4] not in dict_buses:
            dict_buses[words[4]] = [words[0] + " " + words[1] + " " + words[2] + " " + words[3]]
        else:
            dict_buses[words[4]].append(words[0] + " " + words[1] + " " + words[2] + " " + words[3])
        

# go every list and make the dictonaries needed. 
# S[tudent] <lastname> [B[us]]
# T[eacher] <lastname>
# B[us] <number>
# G[rade] <number> [H[igh]]L[ow]]
# A[verage] <number>
# I[nfo]
# Q[uit]
#     0            1         2      3         4    5      6          7
# StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName
def main():
    while True:
        # if running interactively, show prompt, else just read silently (this is for testing)
        if sys.stdin.isatty():
            line = input("please enter a command(S, T, B, G, A, I, Q): ")
        else:
            line = input()

        line = line.strip()

        # Skip empty lines or comments
        if not line or line.startswith("//"):
            continue

        if ":" in line:
            command, rest = line.split(":", 1)
            command = command.strip().lower()[0]
            args = rest.strip().split()
        else:
            command = line.strip().lower()
            args = []

        if command == "q":
            print("exiting")
            return
        
        elif command == "s":
            lastname = args[0].lower()
            option = args[1].lower() if len(args) > 1 else ""
            show_students_by_lastname_dict(lastname.lower(), option.lower())
        
        elif command.lower() == "t":
            Tlastname = args[0].lower()
            print_teachers_students(Tlastname)
        
        elif command.lower() == "g":
            grade = args[0]
            view_h_l = args[1].lower() if len(args) > 1 else ""
            if view_h_l == "high" or view_h_l == "low":
                print_high_low_gpa(grade, view_h_l)
            else:    
                print_by_grade(grade)
        
        elif command.lower() == "b":
            bus_route = args[0]
            print_by_bus_route(bus_route)

        elif command.lower() == "a":
            grade = args[0]
            compute_avg_gpa_for_grade(grade)

        elif command.lower() == "i":
            # print(dict_grade)
            for key, value in dict_grade.items():
                print(f"Grade: {key}, Number of Students: {len(value)}")

if __name__ == "__main__":
    main()
