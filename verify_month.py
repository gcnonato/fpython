list_example_month = [
    '05/01/2020',
    '23/09/2020',
    '05/03/2020',
    '11/05/2020',
    '31/07/2020',
    '31/01/2020',
    '11/08/2020',
    '09/04/2020',
    '03/12/2020'
]

is_january = ['01', '02', '03', '04']
is_may = ['05', '06', '07', '08']

for month in list_example_month:
    if month.split('/')[1] in is_january:
        print(f'month --- 1')
    elif month.split('/')[1] in is_may:
        print(f'month --- 2')
    else:
        print(f'month --- 3')
