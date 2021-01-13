

num = int(input());
stage, keyx = 1, 1

while keyx + stage <= num :
    keyx += stage
    stage += 1;

step = num -keyx
x = step + 1
y = stage - step;

if stage % 2 == 0 :
    print('%d/%d' %(x,y));
else :
    print('%d/%d' %(y,x));

