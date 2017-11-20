with open("sample_txt.txt", encoding="utf-8") as f:
    txt = f.read()
    if txt == "":
        print("Будьте внимательнее! Загруженный вами документ пуст!")
    else:    
        lin = txt.splitlines()
        mn = len(lin[0])
        mx = 0
        c = 0
        for i in enumerate(lin):
            if len(lin[i[0]]) < mn and len(lin[i[0]]) != 0:
                mn = len(lin[i[0]])
            if len(lin[i[0]]) > mx:
                mx = len(lin[i[0]])
            if len(lin[i[0]]) == 0:
                c += 1
        if mn == 0:
            print("Все строки в документе <<нулевые>>, т.е. не содержат символов")
        else:
            otv = mx/mn
            if otv == 1:
                print("Все строки в документе одинаковой длины")
            else:
                print("Самая короткая строка меньше самой длинной в", round(otv, 2), "раз(а)")
            print("<<Нулевые>>, т.е. не содержащие символов строки при подсчете не рассматривались.")
            print("Всего нулевых строк:", c)
