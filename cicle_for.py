school_list=[{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '4b', 'scores': [3,3,4,4,5]}, {'school_class': '4v', 'scores': [4,4,4,5,5]}]


def avg_class (cl,sc_list):
    sum_cl = 0
    for num in sc_list:
        if num['school_class'] == cl:
            for score in num['scores']:
                sum_cl += score
            avg = sum_cl / len(num['scores'])
    return avg


def avg_all(sc_list):
    sum_all = 0
    count = 0
    for num in sc_list:
        for score in num['scores']:
            sum_all += score
        count += len(num['scores'])
    avg = sum_all/count
    return avg


for num in school_list:
    print(num['school_class'] + ': ' + str(avg_class(num['school_class'], school_list)))
print ('School: ' + str(avg_all(school_list)))