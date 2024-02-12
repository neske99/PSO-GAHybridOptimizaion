def g1(x):
    x1=x[0]
    x2=x[1]
    x3=x[2]
    x4=x[3]
    x5=x[4]
    return 85.334407 + 0.0056858*x2*x5 + 0.0006262*x1*x4 - 0.0022053*x3*x5

def g2(x):
    x1=x[0]
    x2=x[1]
    x3=x[2]
    x4=x[3]
    x5=x[4]
    
    return 80.51249 + 0.0071317*x2*x5 + 0.0029955*x1*x2 - 0.0021813*x3**2

def g3(x):
    x1=x[0]
    x2=x[1]
    x3=x[2]
    x4=x[3]
    x5=x[4]

    return 9.300961 + 0.0047026*x3*x5 + 0.0012547*x1*x3 + 0.0019085*x3*x4

def is_feasable(x):
    x1=x[0]
    x2=x[1]
    x3=x[2]
    x4=x[3]
    x5=x[4]
    if x1<78  or x1>102:
        print("x1")
        return False
    if x2<33 or x2>45:
        print("x2")
        return False
        
    if x3<27 or x3>45:
        print("x3")
        return False
    if x4<27 or x4>45:
        print("x4")
        return False
    if x5<27 or x5>45:
        print("x5")
        return False

    g1res=g1(x)
    g2res=g2(x)
    g3res=g3(x)

    if g1res<0 or g1res>92:
        #print("g1")
        return False
    if g2res<90 or g2res>110:
        #print("g2")
        return False
    if g3res<20 or g3res>25:
        #print("g3")
        return False
    
    return True
def himmelblau_fittnes(x):
    x3=x[2]
    x1=x[0]
    x5=x[4]
    toReturn= -(5.3578547*x3**2 + 0.8356891*x1*x5 + 37.293239*x1 - 40792.141)
    g1res=g1(x)
    if g1res>92:
        toReturn+=-((g1res)-92)*1000
    elif g1res<0:
        toReturn+=(g1res)*1000
    
    g2res=g2(x)
    if g2res>110:
        toReturn-=((g2res)-110)*1000
    elif g2res<90:
        toReturn-=(90-(g2res))*1000
    
    g3res=g3(x)
    if g3res>25:
        toReturn-=((g3res)-25)*1000
    elif g3res<20:
        toReturn-=(20-(g3res))*1000
    return toReturn

def actual_himmelblau(x):
    x3=x[2]
    x1=x[0]
    x5=x[4]
    return -(5.3578547*x3**2 + 0.8356891*x1*x5 + 37.293239*x1 - 40792.141)