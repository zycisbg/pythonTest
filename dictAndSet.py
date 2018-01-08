# dict 相当于 hashMap
# dict是用空间来换取时间的一种方法
d = {'laosan': 18, 'laosi': 19, 'laowu': 33, 'laoliu': 99}
d['laoqi'] = 76
print(len(d))

print('laoba' in d)

print(d.get('laoba','laobabuzai'))

# set  相当于 hashSet
persons = ['laosan', 'laosi', 'laowu']
s = set(persons)
s.add('laoqi')
print(s)



