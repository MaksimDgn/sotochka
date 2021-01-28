#!/usr/bin/python
#coding=utf-8
import os
import re
from operator import itemgetter

f = open('/home/maksim/projects/klavogonki/sotochka.txt')


def reslog( znaki=0):
    return "Время: -- знаки {} ".format( znaki)

    
def test():
    snaki=''
    date=[]
    er=''
    i = 0

    sot = {}
    for line in f:
        if line[2:3]=='.':
            date.append(line.strip())
            print(date)
        if line[1:2]==' ':
            er = line
        if line[0:3].isdigit():
            snaki = line
        print("snaki: {} errors: {}".format(snaki, er))
        i+=1
    
        sot['mydata'] = date
        print(sot)
        for i in date:
            print(i)
            
    f.close()

def a(fname):
    fn = fname
    rege_znaki = '\d{3} '
    rege_date = '\d\d.\d\d.\d\d\d\d'
    rege_time = '\d\d:\d\d.\d'
    i = 0
    c = 0
    t = 0
    z = 0
    res_date = {'date': ''}
    res_time = {'{}':''}
    res_date_list = []
    res_time_list = []
    res_znaki_list = []

#    regex = '.'
    for line in fn:
        match_date = re.search(rege_date, line)
        if match_date:
            res_date_list.append('{} date {}'.format(c, match_date.group()))
            c +=1
        #     res_date.update({'date_'+str(c): match_date.group()})
        #     c +=1
        match_t = re.search(rege_time, line)
        if match_t:
            list_t = "{}) match {}".format(t, match_t.group())
            res_time_list.append(list_t)
            # print(t)
            # for k, v in res.items():
            #     print(k, v)
            res_time.update({'{}'.format(t): match_t.group()})
           # res_time_list.extend(match_t.group().strip())
            t +=1
        
        match_date = re.search(rege_znaki, line)
        if match_date:
            res_znaki_list.append('{} znaki {}'.format(z, match_date.group()))
            z +=1
        #     res_date.update({'date_'+str(c): match_date.group()})
        #     c +=1
        match_t = re.search(rege_time, line)
        i +=1
    fn.close
    # print("i: %d"%i)
    # print("c: %d"%c)
    # print("t: %d"%t)
    for d in res_date_list:
        print(d)
    # for k, v in res_date.items():
    #     print(k,v)
   # s = sorted(res_time, key=itemgetter(1))
    # for k, v in res_time.iteritems():
    #     print(k,v)
#    print(res_time_list)
    for k in res_time_list:
        print( k)
    i = 0
    d1 = 0
    d2 = 0
    for k in res_znaki_list:
        d1 = int(re.search("\d{3}", reslog(k)).group())
        d2 =d1+d2
        print( k, d2, i)
        i +=1
    srednee_kol_znakov = d2/(i-1)
    print("Среднее колическо знаков в минуту {} d:{}, i:{}".format(srednee_kol_znakov, d2, i))
    #reslog(time, znaki=0)



def main():
    print('Hello, world!')
    a(f)

    
if __name__=='__main__':
    main()

#228

