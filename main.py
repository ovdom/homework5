tableware = ['ложка', 'чайник', 'кастрюля']
mutable_list = tableware
print('Mutable_list: ', mutable_list)
tableware.append ('мантоварка')
tableware[0] = 'сковородка'
print('Mutable_list: ', mutable_list)
tuple = (1, 'ложка', 5.4, 'стакан', ['сковородка', 'чайник', 'спички'])
immutable_var = tuple
print('Immutable_var: ', immutable_var)
print(tuple[4])
tuple[4][2] = 'кастрюля'
print(tuple[4])
print('Immutable_var: ', immutable_var)
tuple[0] = 2
print('Immutable_var: ', immutable_var)