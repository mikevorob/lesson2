def learn_or_job(age):
    if age<0:
        res='Возраст не может быть отрицательным!!!'
    elif age<7:
        res='Детский сад'
    elif age<16:
        res='Школа'
    elif age<18:
        res='Школа или колледж'
    elif age<22:
        res='Работа или ВУЗ (бакалавриат)'
    elif age<24:
        res='Работа или ВУЗ (магистратура)'
    else:
        res='Работа'
    return res


age=int(input("Введите возраст: "))
res=learn_or_job(age)
print (res)

