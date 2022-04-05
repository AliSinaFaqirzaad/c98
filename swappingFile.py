def swapfiledata():
    file1 = input('enter file name')
    file2 = input('enter file name')
    with open(file1) as a:
        dataa=a.read()

    with open(file2) as b:
        datab=b.read()

    with open(file1,'w') as a:
        a.write(datab)

    with open(file2,'w') as b:
        b.write(dataa)
swapfiledata()