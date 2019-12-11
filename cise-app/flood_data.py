from fake import DataGen
import random

if __name__ == "__main__":
    n = 100
    students = []
    visas = []
    majors = []
    notes = []
    passports = []
    dg = DataGen()

    for i in range(n):
        student = dg.create_student()
        students.append(student)
        curr_sid = student.sid
        visa_rand = random.randint(1,10)
        major_rand = random.randint(1,10)
        note_rand = random.randint(1,10)
        passport_rand = random.randint(1,10)
        
        # create visa
        if(visa_rand < 8):
            visa = dg.create_visa(curr_sid)
            visas.append(visa)

        if(major_rand < 9):
            major = dg.create_major(curr_sid)
            majors.append(major)

        if(note_rand < 7):
            note = dg.create_note(curr_sid)
            notes.append(note)

        if(passport_rand < 10):
            passport = dg.create_passport(curr_sid)
            passports.append(passport)

    for i in range(10):
        print(students[i])
        print(visas[i])
        print(majors[i])
        print(notes[i])
        print(passports[i])
        
