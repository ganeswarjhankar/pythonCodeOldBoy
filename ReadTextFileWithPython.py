file = open('test.txt')
#read all the content of the file
#read n number of character by passing parameters

##print(file.read(1))

#print(file.readline())

#print(file.readline())
#read only one single line  at  a time readline()
#print(file.readline())
#print(file.readline())
#print(file.readline())





#print line by line using readline method
#line = file.readline()
#while line!= "":
    #print(line)
    #line= file.readline()

values = ["abc", "ade","def","ghi","jkl","mnop"]
for line in file.readlines():
    print(line)


file.close()
