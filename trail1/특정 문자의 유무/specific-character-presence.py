string = input()
ee_include = ''
ab_include = ''

if 'ee' in string:
    ee_include = 'Yes'
else :
    ee_include = 'No'

if 'ab' in string:
    ab_include = 'Yes'
else:
    ab_include = 'No'

print(ee_include, ab_include)