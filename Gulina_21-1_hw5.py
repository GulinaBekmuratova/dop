Geektech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
del Geektech['bag']
Geektech['address'] = 'Ibraimova 103'
Geektech['number'] = '0507052018'
Geektech['Instagram'] = 'geektech_kg'

Geektech['courses'].append('UX/UI')
Geektech['courses'] = set(Geektech['courses'])

for key, value in Geektech.items():
    print(f'{key}: {value}')

    
