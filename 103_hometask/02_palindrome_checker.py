print('Введите фразу. Если фраза является палиндромом, то результат будет True, если нет False')
phrase = input()
print(str(phrase).replace(' ', '') == str(phrase).replace(' ', '')[::-1])