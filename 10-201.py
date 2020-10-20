# a = [1,2,3,4]
# for a1 in a:
#     # if a1 is not 3:
#     if a1 != 3:
#         print(a1)

def b(b1,b2=True):
    if b2:
        print("b2 is true")
    else :
        print("b2 is not true")

if __name__ == '__main__':
    # b(1,False)
    a = [1,2,3]
    b=reversed(a)
    print(a)
    # print(b)
    for b1 in b:
        print(b1)