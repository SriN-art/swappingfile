def swapfiledata():
    filename1 = input('Enter the file name one: ')
    filename2 = input('Enter the file name two: ')
    file1 = open(filename1, 'r')
    file2 = open(filename2, 'r')

    data_a=file1.read()
    data_b=file2.read()

    file1=open(filename1,'w')
    file1.write(data_b)

    file2=open(filename2, 'w')
    file2.write(data_a)
swapfiledata()
