
choice = int(input('Введіть 1 або 2: '))
while choice != 1 or 2:
    if choice == 1:
        text = input("Введіть текст: ")
        d = {}
        for i in text:
            if i.isalpha():
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
        for i in sorted(d):
            print(i, d[i])

    if choice == 2:
        text = input('Введіть текст: ')
        a = text.split()
        b = list(set(a))
        c = sorted(b)
        text = [x for x in c if len(x) > 3]
        print(text)

    choice = int(input('Введіть 1 або 2: '))