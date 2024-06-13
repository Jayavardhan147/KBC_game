questions = [
          #question of your choice
    [
        "Which language was used to create fb?", "Python", "French",
        "JavaScript", "Php", "None", 4
    ],
    [
        "Current Railway Minister of India is", "Mamta Banarjee", "Ram Vilash",
        "Ashwini Vaishnaw", "Piyush Goyal", 3
    ],
    [
        "The International Literacy Day is observed on", "Sep 8", "Nov 28",
        "May 2", "Sep 22", 1
    ],
    [
        "Which god is also known as ‘Gauri Nandan’?", "Agni", "Indra",
        "Hanuman", "Ganesha", 4
    ],
    [
        "What does not grow on tree according to a popular Hindi saying?",
        "Money", "Flowers", "Leaves", "Fruits", 1
    ],
    [
        "The language of Lakshadweep. a Union Territory of India, is", "Tamil",
        "Hindi", "Malayalam", "Telugu", 3
    ],
    [
        "In which group of places the Kumbha Mela is held every twelve years?",
        "Ujjain. Purl; Prayag. Haridwar", "Prayag. Haridwar, Ujjain,. Nasik",
        "Rameshwaram. Purl, Badrinath. Dwarika",
        "Chittakoot, Ujjain, Prayag,'Haridwar", 2
    ],
    [
        "Bahubali festival is related to", "Islam", "Hinduism", "Buddhism",
        "Jainism", 4
    ],
    [
        "September 27 is celebrated every year as", "Teachers' Day",
        "National Integration Day", "World Tourism Day",
        "International Literacy Day", 3
    ],
    [
        "Who is the author of the epic 'Meghdoot'?", "Vishakadatta", "Valmiki",
        "Banabhatta", "Kalidas", 4
    ],
    [
        "The death anniversary of which of the following leaders is observed as Martyrs' Day?",
        "Smt. Indira Gandhi", "PI. Jawaharlal Nehru", "Mahatma Oandhi",
        "Lal Bahadur Shastri", 3
    ]
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000] #game levels
money = 0
for i in range(0, len(questions)):

  question = questions[i]
  print(f"\nQuestion for Rs. {levels[i]}")
  # to print question
  print(question[i])
  # to print Options
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n"))
  if (reply == 0):
    money = levels[i - 1]
    break
  if (reply == question[-1]):
    print(f"\nCorrect answer, you have won Rs. {levels[i]}")
    if (i == 4):
      money = 10000
    elif (i == 9):
      money = 320000
    elif (i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break

print(f"\nYour take home money is {money}")
