ItemIncart = 0
#2 items will be added to the cart

if ItemIncart != 2: #raise Exception("Product cart count not matching")
    pass


assert(ItemIncart == 0)

#try ,
#catch




try:
    with open('test.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally: # to clean cookies and all
    print("cleaning up records")









