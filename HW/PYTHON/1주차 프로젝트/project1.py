import os
import sys


###################### 파일을 한줄씩 읽어서 리스트에 추가하는 함수 ######################


def readline_and_append(readed_file):
    for line in readed_file:
        first_name = line.split()[2].lower()  # "gildong"
        full_name = line.split()[1] + " " + \
            line.split()[2]  # "Hong Gildong"
        stu_number_name_mid_final_list = [line.split()[0], full_name, int(line.split()[3]), int(line.split()[
            4])]  # ["20180001","Hong Gildong", 84, 73]
        # gildong = ["20180001","Hong Gildong", 84, 73] 형태로도 저장됨
        globals()[first_name] = stu_number_name_mid_final_list
        # 중첩 리스트 형식으로도 저장
        stu_list.append(stu_number_name_mid_final_list)
    return


###################### 평균구하기 함수 ######################


def get_average(mid, final):
    return (mid + final)/2

###################### 학점구하기 함수 ######################


def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    elif score >= 70 and score < 80:
        return 'C'
    elif score >= 60 and score < 70:
        return 'D'
    else:
        return "F"

###################### 표 윗 부분 출력해주는 함수 ######################


def print_table_row():
    print("Student" + "\t\t" + "Name" + "\t\t" + "Midterm" + "\t" +
          "Final" + "\t" + "Average" + "\t" + "Grade")
    print("-" * 70)
    return


###################### show 함수 ######################


def show():
    print_table_row()
    for student in stu_list:
        print(student[0] + "\t" + student[1] + "\t" + str(student[2]) + "\t" +
              str(student[3]) + "\t" + str(student[4]) + "\t" + student[5])
    return

###################### search 함수 ######################


def search():
    student_id = input('Student ID: ')
    for student in stu_list:
        if student[0] == student_id:
            print_table_row()
            print(student[0] + "\t" + student[1] + "\t" + str(student[2]) + "\t" +
                  str(student[3]) + "\t" + str(student[4]) + "\t" + student[5])
            return  # 찾으면 함수를 종료시켜 버린다.
    print("NO SUCH PERSON.")  # for 문을 다 돌때까지 찾지 못하면 "NO SUCH PERSON."을 띄운다.
    return


###################### change_score 함수 ######################

def change_score():
    student_id = input('Student ID: ')
    for student in stu_list:
        if student[0] == student_id:
            mid_or_final = input('Mid/Final? ')
            if mid_or_final == "mid":  # 중간고사일 때,
                new_score = int(input("Input new score: "))
                if new_score <= 100:
                    # 바뀌기 이전 score 출력
                    print_table_row()
                    print(student[0] + "\t" + student[1] + "\t" + str(student[2]) + "\t" +
                          str(student[3]) + "\t" + str(student[4]) + "\t" + student[5])

                    student[2] = new_score  # 중간고사 점수 수정
                    student[4] = get_average(
                        student[2], student[3])  # 평균점수 다시 계산
                    student[5] = get_grade(student[4])  # Grade 다시 계산

                    # 바뀐 후 score 출력
                    print("Score changed.")
                    print(student[0] + "\t" + student[1] + "\t" + str(student[2]) + "\t" +
                          str(student[3]) + "\t" + str(student[4]) + "\t" + student[5])

                    # 전체 리스트 다시 정렬
                    stu_list.sort(key=lambda e: e[4], reverse=True)
                    return
                else:
                    return

            elif mid_or_final == "final":  # 기말고사일 때,
                new_score = input("Input new score: ")
                if new_score <= 100:
                    student[3] = new_score  # 기말고사 점수 수정
                    student[4] = get_average(
                        student[2], student[3])  # 평균점수 다시 계산
                    student[5] = get_grade(student[4])  # Grade 다시 계산
                    # 전체 리스트 다시 정렬
                    stu_list.sort(key=lambda e: e[4], reverse=True)
                    return
                else:
                    return
            else:
                return

    print("NO SUCH PERSON.")  # for 문을 다 돌때까지 찾지 못하면 "NO SUCH PERSON."을 띄운다.
    return


###################### add 함수 ######################


def add():
    existing_id_list = []
    for student in stu_list:
        existing_id_list.append(student[0])  # 이미 존재하는 학번 리스트를 만든다.
    input_id = input("Student ID: ")
    # 이미 학번 존재하면 함수를 return 해버린다.
    if input_id in existing_id_list:
        print("ALREADY EXISTS")
        return
    # 학번이 중복되지 않는 것이 확인되었으므로, 나머지 정보도 입력받는다.
    input_name = input("Name: ")
    input_midterm_score = int(input("Midterm Score: "))
    input_final_score = int(input("Final Score: "))
    # 평균과 학점을 계산한다.
    averge_score = get_average(input_midterm_score, input_final_score)
    grade = get_grade(averge_score)
    # 새로운 학생의 정보 리스트를 만든다.
    new_student_info_list = [
        input_id, input_name, input_midterm_score, input_final_score, averge_score, grade]
    # stu_list에 추가한다.
    stu_list.append(new_student_info_list)
    # 전체 학생 리스트를 평균 순으로 다시 정렬한다.
    stu_list.sort(key=lambda e: e[4], reverse=True)
    print("Student added.")
    return

###################### searchgrade 함수 ######################


def search_grade():
    existing_grade_list = []
    for student in stu_list:
        if student[5] not in existing_grade_list:
            existing_grade_list.append(student[5])  # 이미 존재하는 학번 리스트를 중복없이 만든다.
    # 찾고있는 학점을 입력받는다.
    grade_to_search = input('Grade to search: ')
    # "A", "B", "C", "D", "F" 중 하나가 아니라면, return 한다.
    if grade_to_search not in ["A", "B", "C", "D", "F"]:
        return
    # 학생들의 학점 중에 없다면, return 한다.
    elif grade_to_search not in existing_grade_list:
        print("NO RESULTS.")
        return
    else:
        searching_grade_student_list = []
        for student in stu_list:
            if student[5] == grade_to_search:
                searching_grade_student_list.append(student)
        for student in searching_grade_student_list:
            print(student[0] + "\t" + student[1] + "\t" + str(student[2]) + "\t" +
                  str(student[3]) + "\t" + str(student[4]) + "\t" + student[5])
        return
    return


###################### 실행되는 부분(메인함수) ######################

while(True):
    # 파일 읽어오기 및 데이터 저장하기
    if len(sys.argv) == 1:  # 사용자가 뒤에 아무것도 입력하지 않았을 때,
        file_name = ""
    else:
        file_name = sys.argv[1]  # 사용자가 뒤에 파일명을 입력했을 때,
    # stu_list를 선언해준다. 나중에 stu_list = [["20180001","Hong Gildong", 84, 73], ["20180001","Hong Gildong", 84, 73], ...]
    stu_list = []

    # input 받은 파일명에 따라 실행되는거 분류

    if file_name == "":
        with open("students.txt", "r") as fr:
            readline_and_append(fr)
            break

    elif os.path.exists(file_name):
        with open(file_name, "r") as fr:
            readline_and_append(fr)
            break
    else:
        print('File not Found')
        # 종료 시키기
        sys.exit()

# stu_list에 Average, Grade 추가하기
# [["20180001","Hong Gildong", 84, 73] , [~~], ...] --> [["20180001","Hong Gildong", 84, 73, 78.5, "C"], [~~],...]
for student in stu_list:
    student_average_score = get_average(student[2], student[3])
    student_grade = get_grade(student_average_score)
    student.append(student_average_score)
    student.append(student_grade)

# stu_list 평균 점수를 기준으로 내림차순 정렬
stu_list.sort(key=lambda e: e[4], reverse=True)

# 프로그램 실행시키면 출력되는 화면

print_table_row()
for student in stu_list:
    print(student[0] + "\t" + student[1] + "\t" + str(student[2]) + "\t" +
          str(student[3]) + "\t" + str(student[4]) + "\t" + student[5])

# 명령어 기다리기

while(True):
    upper_input_command = input("# ").upper()
    if upper_input_command == "SHOW":
        show()
    elif upper_input_command == "SEARCH":
        search()
    elif upper_input_command == "CHANGESCORE":
        change_score()
    elif upper_input_command == "ADD":
        add()
    elif upper_input_command == "SEARCHGRADE":
        search_grade()
    elif upper_input_command == "REMOVE":
        print("remove")
    elif upper_input_command == "QUIT":
        break
    else:
        continue
