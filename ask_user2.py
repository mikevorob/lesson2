#def ask_user():
    #answer="sdwer"
    #while answer!='Хорошо':
        #answer=input('Как дела? ')
dic={"Как дела?" : "Хорошо!", "Что делаешь?" : "Программирую", "Какие планы?" : "Дальше программировать", "В кино пойдешь?" : "Не могу, программировать надо", "Привет" : "И тебе привет", "Пока" : "Бывай"}

def talk():
	question=None
	while question!="Пока":
		question=input()
		if question in dic.keys():
			print (dic[question])
		else:
			print ("Вопрос не понят!")


talk()