def ask_user():
    answer=None
    try:
       while answer!='Хорошо':
          answer=input('Как дела? ')
    except KeyboardInterrupt:
        print("Пока")


ask_user()