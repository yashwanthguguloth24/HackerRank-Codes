rows,cols = input().split()
rows = int(rows)
cols = int(cols)
c = '.|.'

#top part
for i in range(rows//2):
    print((c*i).rjust((cols//2)-1,'-')+c+(c*i).ljust((cols//2)-1,'-'))

#middle part
print('WELCOME'.center(cols,'-'))

#bottom part
for i in reversed(range(0,rows//2)):
    print((c*i).rjust((cols//2)-1,'-')+c+(c*i).ljust((cols//2)-1,'-'))