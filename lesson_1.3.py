# Реализовать склонение слова «процент» для чисел до 20. Например,
# задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.

word_mod1 = 'процент'
word_mod2 = 'процента'
word_mod3 = 'процентов'
for i in range(1, 21):
    if i == 1:
        print(i, word_mod1)
    elif 2 <= i <= 4:
        print(i, word_mod2)
    else:
        print(i, word_mod3)
