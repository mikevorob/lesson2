def ask_user():
    answer="sdwer"
    try:
       while answer!='Хорошо':
          answer=input('Как дела? ')
    except KeyboardInterrupt:
        print("Пока")


ask_user()