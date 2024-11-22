def moon_weight(w0,w,y):
    for x in range(0,y+1):
        print(x,(w0+w*x)*0.165)

moon_weight(90, 0.25,5)
