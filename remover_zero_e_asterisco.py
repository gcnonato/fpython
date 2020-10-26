nro = '009**987677*66'
nv_nro = ''
for n in nro:
    if n != str(0) and n != '*':
        nv_nro += n
    if n == '*':
        nv_nro += 'NULL'
print(nv_nro)

