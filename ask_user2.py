#def ask_user():
    #answer="sdwer"
    #while answer!='Хорошо':
        #answer=input('Как дела? ')
dic={"Как дела?" : "Хорошо!", "Что делаешь?" : "Программирую", "Какие планы?" : "Дальше программировать", "В кино пойдешь?" : "Не могу, программировать надо", "Привет" : "И тебе привет", "Пока" : "Бывай"}

def talk():
	ask="wedw"
	while ask!="Пока":
		ask=input()
		if ask in dic.keys():
			print (dic[ask])
		else:
			print ("Вопрос не понят!")


talk()