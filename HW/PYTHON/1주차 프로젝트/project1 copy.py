import os
import sys


###################### 파일을 한줄씩 읽어서 리스트에 추가하는 함수 ######################


def readline_and_append(readed_file):
    for line in readed_file:
        set first name from line
        set full name from line
        # ["20180001","Hong Gildong", 84, 73]
        stu_number_name_mid_final_list = [id, full name, mid_score, final_score]
        # gildong = ["20180001","Hong Gildong", 84, 73] 형태로도 저장됨
        first_name = stu_number_name_mid_final_list  # 변수값을 리스트의 변수명으로 사용할 예정 -> 찾아봐야할 듯
        # 중첩 리스트 형식으로도 저장
        append stu_number_name_mid_final_list to stu_list
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
        print student  # student 안에는 학번, 이름, 중간고사성적, 기말고사 성적, 평균, 학점이 들어가있다.
    return


###################### search 함수 ######################


def search():
    set student_id user_input
    for student in stu_list:
        if student's id == user_input_student_id
          print_table_row()
           print student's information
            return  # 찾으면 함수를 종료시켜 버린다.
    print "NO SUCH PERSON."  # for 문을 다 돌때까지 찾지 못하면 "NO SUCH PERSON."을 띄운다.
    return


###################### change_score 함수 ######################

def change_score():
    set student_id user_input
    for student in stu_list:
        if there is student_id match to student_list
          ask mid_or_final
           if answer is mid
              ask new_score
               if valid score
                  # 바뀌기 이전 score 출력
                  print_table_row()
                   print student information

                    student's mid_score = new_score  # 중간고사 점수 수정
                    student's average score = get_average(
                        mid score, final score)  # 평균점수 다시 계산
                    recalculate the grade by new scores  # Grade 다시 계산

                    # 바뀐 후 score 출력
                    print "Score changed."
                    print new_student_info

                    # 전체 리스트 다시 정렬
                    rearrage the list
                    return
                else:
                    return

            elif answer is final:  # 기말고사일 때,
                ask new score
                if valid score:
                    student's final score = new_score  # 기말고사 점수 수정
                    student's average score = get_average(
                        student_mid, student_final)  # 평균점수 다시 계산
                    recalculate the grade  # Grade 다시 계산
                    # 전체 리스트 다시 정렬
                    rearrange the entire list
                    return
                else:
                    return
            else:
                return

    print "NO SUCH PERSON."   # for 문을 다 돌때까지 찾지 못하면 "NO SUCH PERSON."을 띄운다.
    return


###################### add 함수 ######################


def add():
    existing_id_list
    for student in stu_list:
        append id to existing_id_list  # 이미 존재하는 학번 리스트를 만든다.
    set input_id by user_input
    # 이미 학번 존재하면 함수를 return 해버린다.
    if input_id in existing_id_list:
        print "ALREADY EXISTS"
        return
    # 학번이 중복되지 않는 것이 확인되었으므로, 나머지 정보도 입력받는다.
    set input_name by user_input
    set input_midterm_score by int(user_input)
    input_final_score = int(user_input)
    # 평균과 학점을 계산한다.
    calculate averge_score = get_average(input_midterm_score, input_final_score)
    grade = get_grade(averge_score)
    # 새로운 학생의 정보 리스트를 만든다.
    set new_student_info_list with
      [input_id, input_name, input_midterm_score, input_final_score, averge_score, grade]
    # stu_list에 추가한다.
    stu_list.append(new_student_info_list)
    # 전체 학생 리스트를 평균 순으로 다시 정렬한다.
    rearrange_entire_stu_list by average_score
    print "Student added."
    return

###################### searchgrade 함수 ######################


def search_grade():
    existing_grade_list = []
    for student in stu_list:
        if student's id does not exist in in existing_grade_list
          append student id to existing_grade_list # 이미 존재하는 학번 리스트를 중복없이 만든다.
    # 찾고있는 학점을 입력받는다.
    set grade_to_search by user_input
    # "A", "B", "C", "D", "F" 중 하나가 아니라면, return 한다.
    if grade_to_search not in ["A", "B", "C", "D", "F"]:
        return
    # 학생들의 학점 중에 없다면, return 한다.
    elif grade_to_search does not exist in existing_grade_list:
        print "NO RESULTS."
        return
    else:
        searching_grade_student_list = []
        for student in stu_list:
            if student's grade same with grade_to_search:
                append student to searching_grade_student_list
        for student in searching_grade_student_list:
            print student info
        return
    return

###################### remove 함수 ######################


def remove():
    # 목록에 아무도 없을 경우, return 한다.
    if list is empty:
        print("List is empty.")
        return

    # 학번 리스트를 만든다.
    existing_id_list = []
    for student in stu_list:
        append student id to existing_id_list

    # 학번을 입력받는다.
    set input_id by user_input_id
    if input_id not in existing_id_list:
        print "NO SUCH PERSON."
        return
    else:
        for student in stu_list:
            if student id same to input_id:
                stu_list.remove(student)
                break
        print("Student removed.")
        return


###################### quit 함수 ######################


def quit():
    ask yes_or_no and set save_data_yes_or_no by user_input
    if save_data_yes_or_no == "yes":
        ask file_name_to_write and set variable by user_input
        open file to write by file name: file_name_to_write
        for student in stu_list:
            print student info
            write data to writing file
        close file
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
        remove()
    elif upper_input_command == "QUIT":
        quit()
        break
    else:
        continue
