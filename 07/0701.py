def moon_weight(w0,w):
    for x in range(0,16):
        print(x,(w0+w*x)*0.165)

moon_weight(40, 1)
