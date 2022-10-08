print('Введите набор скобок (), {}, []. Если все скобки закрыты, то результат будет True, если нет False')
s = input()

stack = []
ht = {"}": "{", ")": "(", "]": "["}
for p in s:
    if p in ht.values():
        stack.append(p)
    elif p in ht and ht[p] in stack:
        stack.remove(ht[p])
    else:
        print('False')
        exit()
print(len(stack) == 0)
