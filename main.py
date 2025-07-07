# დავალება1. დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს რიცხვს, რა რიცხვსაც გადავცემთ, იმდენჯერ შეეკითხება მომხმარებელს
#    სახელს, გვარს და ასაკს. ანუ თუ გადავეცით 3, 3-ჯერ შეეკითხება მომხმარებელს აღნიშნულ ინფორმაციას, ინფუთის
#    საფუძველზე csv ფაილში ჩაწერეთ შესაბამისი ინფორმაცია შემდეგი სახით, მაგალითად:
#   გამოიყენეთ try, ecxept იმისათვის რომ მომხმარებელმა ასაკის შემოყვანის დროს აუცილებლად ინტეჯერი შემოიყვანოს!
#    ფაილში ჩასაწერად აუცილებლად გამოიყენეთ csv მოდულიდან writer და DictWriter!
import csv

# def persons_file(n):
#     import csv
#     person = []
#     counter = 0
#
#     for i in range(n):
#         first_name = input("Enter first name: ")
#         last_name = input("Enter last name: ")
#         while True:
#             try:
#                 age = int(input("Enter age: "))
#                 break
#             except ValueError:
#                 print("Please enter only integer")
#
#         counter += 1
#         person.append({"ID" : counter, "first_name": first_name, "last_name": last_name, "age" : age})
#     print(person)
#
#     with open("persons.csv", "w", newline="") as csvfile:
#         headers = ["ID", "first_name", "last_name", "age"]
#         writer = csv.DictWriter(csvfile, fieldnames=headers)
#         writer.writeheader()
#         writer.writerows(person)
#
#         return csvfile
#
# print(persons_file(int(input("Enter the amount of the persons: "))))




# 2. მიმაგრებულ students.csv ფაილიდან წაიკითხეთ ინფორმაცია, გაფილტრეთ Grade-ის მიხედვით შემდეგნაირად:
#    ყველა სტუდენტი, რომელსაც 50-ზე ნაკლები ქულა აქვს შეინახეთ ახალ ფაილში(failed_students.csv)
#    ყველა სტუდენტი, რომელსაც 50-ზე მეტი ქულა აქვს შეინახეთ ახალ ფაილში(passed_students.csv)
#    ფაილებიდან ინფორმაციის წასაკითხად და ჩასაწერად აუცილებლად გამოიყენეთ DictReader და DictWriter!



def students_grades():
    with open("students.csv", "r") as grade_csv_file:
        reader = csv.reader(grade_csv_file)
        next(reader)

        failed_students = []
        passed_students = []
        students = list(reader)

        passed_students = list(filter(lambda student : int(student[3]) >= 50, students))
        failed_students = list(filter(lambda student : int(student[3]) < 50, students))

        # ჩავამატოთ ახალ ფაილში ჩაჭრილი სტუდენტების სია
        with open("failed_students.csv", "w", newline="") as failed_student_list:
            writer = csv.writer(failed_student_list)
            writer.writerows(failed_students)

        # ჩავამატოთ ახალ ფაილში ჩაბარებული სტუდენტების სია
        with open("passed_students.csv", "w", newline="") as passed_student_list:
            writer = csv.writer(passed_student_list)
            writer.writerows(passed_students)

    return  passed_students, failed_students
print(students_grades())
    # # # create and append failed students



