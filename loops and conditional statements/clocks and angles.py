def main():
    t = int(input())
    while t >0:
        h,m = map(int,input().split())
        angleHr = 0.5 * (60*h+m)
        angleMn = 6*m
        angleBet = 0.5 * (60*h-11*m)
        if angleBet > 180:
            angleBet = 360 - angleBet
        print(int(abs(angleBet)))
        t-=1

if __name__ =="__main__":
    main()