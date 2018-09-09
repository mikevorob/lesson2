list=[{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '4b', 'scores': [3,3,4,4,5]}, {'school_class': '4v', 'scores': [4,4,4,5,5]}]


def avg_class (cl):
	sum=0
	for num in list:
		if num['school_class']==cl:
			for score in num['scores']:
				sum+=score
			avg=sum/len(num['scores'])
	return avg


def avg_all():
	sum=0
	count=0
	for num in list:
		for score in num['scores']:
			sum+=score
		count+=len(num['scores'])
	avg=sum/count
	return avg

print ('4a: '+str(avg_class('4a')))
print ('4b: '+str(avg_class('4b')))
print ('4v: '+str(avg_class('4v')))
print ('School: '+str(avg_all()))