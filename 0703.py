import sys
def moon_weight():
    print('Please enter your current Earth weight')
    w0 = int(sys.stdin.readline())
    print('Please enter the amount your weight might increase each year')
    w = float(sys.stdin.readline())
    print('Please enter the number of years')
    y = int(sys.stdin.readline())
    for x in range(0,y+1):
        print(x,(w0+w*x)*0.165)

moon_weight()
