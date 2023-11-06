import random
import time

from utils import get_word

# Choose a random word
spy_word = get_word()

try:
    participants_count = int(input("Количество участников:").strip())
except:
    print("Неправильное количество участников")
    participants_count = 0
    exit()
try:
    spy_count = int(input("Количество шпионов:").strip())
except:
    print("Неправильное количество шпионов")
    spy_count = 0
    exit()
if spy_count >= participants_count:
    print("Количество шпионов не может больше либо равно количеству участников")
    exit()

# Create a list for participants
participants = [f"Участник {u + 1}" for u in range(participants_count + 1)]

# Member indexes that will be spies
spy_indexes = []
while len(spy_indexes) < spy_count:
    spy_index = random.randint(0, participants_count)
    if spy_index not in spy_indexes:
        spy_indexes.append(spy_index)

print("Игра началась...")

for i in range(participants_count):
    input()
    if i not in spy_indexes:
        msg = f"Загаданное слово: {spy_word}"
    else:
        msg = "Вы шпион"
    print(f"\r{participants[i]}: {msg}", end="", flush=True)
    time.sleep(3)
    print("\r" + " " * 50, end="")  # Clear the line
    time.sleep(0.1)  # Pause to make sure the line has time to clear

# Clear the console before printing "Done!"
print("\r" + " " * 50, end='')  # Clear the line
print(f"Задает вопрос {participants[random.randint(0, participants_count)]}")
