import time
import os
import random
import subprocess

random.seed(29)

# Fungsi untuk membersihkan layar
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Warna terminal
colors = [
    "\033[31m",  # merah
    "\033[32m",  # hijau
    "\033[33m",  # kuning
    "\033[34m",  # biru
    "\033[35m",  # magenta
    "\033[36m",  # cyan
    "\033[38;5;205m",  # pink
]
RESET = "\033[0m"

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# --- Awal Animasi ---
clear()
slow_print(f"{colors[2]}🎉 Selamat Datang di Program Spesial Ulang Tahun Untuk Mamiii! 🎉{RESET}")
time.sleep(1.2)
clear()

slow_print(f"{colors[5]}Hari Ini Adalah Hari Yang Istimewa...{RESET}")
time.sleep(1)
slow_print(f"{colors[4]}Karena Seseorang Yang Sangat Berarti Bagi Kami Sedang Berulang Tahun 💖{RESET}")
time.sleep(1.5)
clear()

slow_print(f"{colors[1]}🎂 Selamat Ulang Tahun Mamiii! 🎂{RESET}", 0.08)
time.sleep(0.7)
slow_print(f"{colors[2]}Semoga Panjang Umur, Sehat Selalu, Dan Penuh Kebahagiaan.{RESET}", 0.06)
slow_print(f"{colors[4]}Terima Kasih Sudah Menjadi Ibu Yang Hebat Dan Luar Biasa. 💕", 0.06)
time.sleep(1)

# Efek “kembang api”
clear()
for i in range(3):
    color = random.choice(colors)
    print(f"{color}✨🎆🎇  HAPPY BIRTHDAY!!!  🎇🎆✨{RESET}")
    time.sleep(0.6)
    clear()
    time.sleep(0.3)

slow_print(f"{colors[5]}Makasih Banyak Ya Mi Dah Jagain Dan Besarin Kami Selama ini 💐{RESET}")
slow_print(f"{colors[2]}Maaf Cuman Bisa Kasih Ini Doangg... 💐{RESET}")
slow_print(f"{colors[4]}Selamat Ulang Tahun Miii! 🎉🥰{RESET}")
print()
clear()

# Emoji random dan warna berubah-ubah
emojis = ["🎂", "🎉", "💖", "🌸", "💐", "🎁", "❤️", "🌹", "🕯️", "✨"]
width = os.get_terminal_size().columns

for i in range(1, 100):
    space = " " * random.randint(1, width - 5)
    emoji_line = "".join(random.choices(emojis, k=random.randint(1, 2)))
    color = random.choice(colors)  # pilih warna acak setiap line

    if i % 10 == 0:
        print(space + f"{color}{emoji_line} Selamat Ulang Tahun Mamii {emoji_line}{RESET}")
    else:
        print(space + f"{color}{emoji_line}{RESET}")

    if i % random.randint(3, 6) == 0:
        print()

    time.sleep(0.2)

# Panggil script selanjutnya
subprocess.run(["python", "Mami.py"])
