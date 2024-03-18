import random
import glob

words = []
file = glob.glob("*.txt")
text_file = open(file[0], 'r')
while True:
    right_text = ""
    text = text_file.readline(1000)
    if text == "":
        break
    else:
        if "\n" not in text:
            words.append(text)
        else:
            index = len(text)
            for i in range(index - 1):
                right_text += text[i]
            words.append(right_text)


wrong = 0
wrong_de = []
wrong_en = []
my_wrong = []

a = int(len(words) / 2 - 1)
while True:
    while True:
        number = random.randint(0, a)
        if number % 2 == 0:
            break
    print(words[number])
    answer = input(":")
    if answer == words[number + 1]:
        print("correct\n\n\n")
        words.remove(words[number])
        words.remove(words[number])
        a = a - 1
        if len(words) == 0:
            print("you win")
            break
    else:
        print("Wrong. Right:", words[number + 1], "\n\n\n")
        wrong_en.append(words[number])
        wrong_de.append(words[number + 1])
        my_wrong.append(answer)
        wrong = wrong + 1
print("\nWrongs:", wrong, "\n")
for i in range(wrong):
    print(str(i + 1) + ".")
    print(wrong_de[i])
    print(wrong_en[i])
    print("Your answer was", my_wrong[i], "\n\n")
