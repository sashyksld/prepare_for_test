import random
import glob

words = []                              # Making a list where we will have a words
file = glob.glob("*.txt")               # Find a txt document where we wrote all words
text_file = open(file[0], 'r')          # Open it
while True:
    right_text = ""
    text = text_file.readline(1000)     # read line in txt document
    if text == "":
        break
    else:
        if "\n" not in text:
            words.append(text)
        else:
            index = len(text)
            for i in range(index - 1):
                right_text += text[i]
            words.append(right_text)     # add a words in list

wrongs = 0                               # we will count the wrongs
wrong_questions = []
wrong_answers = []
my_wrongs = []

a = int(len(words) / 2 - 1)
while True:
    while True:
        number = random.randint(0, a)
        if number % 2 == 0:             # we find the question line, they are odd 1,3,5
            break
    print(words[number])                # we print the question
    answer = input(":")                 # user must answer
    if answer == words[number + 1] or words[number + 1].capitalize():     # if correct:
        print("correct\n\n\n")          # write him correct
        for i in range(2):
            words.remove(words[number])  # remove the question and the answer, the answer comes later than the question
        a = a - 1
        if len(words) == 0:              # if there are no more questions, the user wins and we write results
            print("you win!!!\n\n\n")
            break
    else:
        print("Wrong. Right:", words[number + 1], "\n\n\n")     # here we write him the correct answer for next time
        wrong_questions.append(words[number])
        wrong_answers.append(words[number + 1])
        my_wrongs.append(answer)
        wrongs = wrongs + 1     # this continues until the user answers everything correctly


print("Wrongs:", wrongs, "\n")  # In end, we will have our false answers
for i in range(wrongs):
    print(str(i + 1) + ".")
    print(wrong_questions[i], ":", wrong_answers[i])
    print("Your answer was", my_wrongs[i], "\n\n")
