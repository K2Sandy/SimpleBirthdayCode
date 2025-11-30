import subprocess
import time

questions = ("Kapan Ulang Tahun Adek?",
             "Kapan Ulang Tahun Rara?",
             "Apa Jurusan Kuliah Rara?",
             "Apa Jurusan Kuliah Adek?",
             "Siapa Yang Paling Disayang Rara dan Kaka")
options = (("A. 1 Januari", "B. 5 Maret", "C. 14 Juli", "D. 27 Desember"),
           ("A. 29 November", "B. 13 Agustus", "C. 4 September", "D. 21 Februari"),
           ("A. Teknik Mesin", "B. Kedokteran", "C. Akuntansi", "D. Manajemen"),
           ("A. Informatika", "B. Teknik Sipil", "C. Matematika", "D. Arsitektur"),
           ("A. Aya", "B. Mami", "C. Ms. Febby", "D. Andri"))

guesses = []
Answers = ("D","C","D","A","B")
score = 0

question_number = 0

print(" 💖💖 Quiz Spesial Ulang Tahun Mami 💖💖 ")
print(" Coba Jawab Mi, Seberapa Kenal Mami Sama Adek dan Rara... 💕 ")

for question in questions:
    print()
    print("✨🎈 ----------------------- 🎈✨")
    print(question)
    for option in options [question_number]:                 #beceause it is a 2d tuple then it need index to
       print(option)
    
    guess = input("Enter Your Answer (A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == Answers[question_number]:
        score += 1
        print("Betulll, Hebat Mamiii 💕👏")
    else:
        print("Salahh")
        print(f"The Answer is {Answers[question_number]}")

    question_number += 1  

print()
print("🌹 ----------------------- 🌹")
print("             RESULTS          ")
print("🌹 ----------------------- 🌹")

print(f"Answer :",end=" ")
for answer in Answers:
    print(answer, end=" ")
print()

print(f"Guesses :",end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
    

score = int(score/ len(questions) * 100)
print(f"Your Score is {score}%")
if score < 20:
    print("You Should Let Him Go")
else:
    print()
    print("🌟🎉 HEBAT MAMI!!! 🎉🌟")
    print("💐 Semua jawabannya benarr!! 😍👏")

print("\n🎈🎈 Selamat Ulang Tahun, Mami Tercinta!!! 🎈🎈")
print("💝 Semoga panjang umur, sehat selalu, dan selalu bahagia! 💝")


time.sleep(3)
subprocess.run(["python", "Birthday1.py"])



    