def safe_in(score):
    
    if score<0 or score>100:
        return "Invalid"
    elif score>=97: 
            return "A+"
    elif score>=90: 
        return "A"
    elif score>=80: 
        return "B"
    elif score>=70: 
        return "C"
    elif score>=60: 
        return "D"
    elif score<60: 
        return "F"
    else:
        return None

score=[120,100,90,80,55,67,10,-1,-0]

for sc in score:
    print(repr(sc),"->", safe_in(sc))

    
