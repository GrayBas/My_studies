#import sys
#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['django chto  eto takoe    poryadok ustanovki',
          'model mtv   marshrutizaciya funkcii  predstavleniya',
          'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
for i, row in enumerate(lst_in):
    while row.count('  '):
        row = row.replace('  ', ' ')
    row = row.replace(' ', '-')

    lst_in[i] = row


print(*lst_in, sep='\n')
