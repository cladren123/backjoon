def han(n) :
    man = [];
    if n < 10 :
        return 1;
    else :
        n = list(str(n));
        for i in range(0,len(n)-1) :
            gon = int(n[i]) -int(n[i+1])
            man.append(gon);
        man = set(man);
        print(man)

        if len(man) == 1 :
            return 1;
        else :
            return 0;

print(han(111))