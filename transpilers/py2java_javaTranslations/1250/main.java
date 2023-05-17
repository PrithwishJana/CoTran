import copy;
var a = list ( map ( int , input ( ) . split ( ) ) );
var ans = 0;
for i in range ( 0 , 14 ) :
    x = copy . copy ( a );
    n = a { i } // 14;
    r = a { i } % 14;
    x { i } = 0;
    for j in range ( 0 , 14 ) :
        x { j } += n;
    if (r >= 13 - i) {
        for j in range ( i + 1 , 14 ) :
            x { j } += 1;
        for j in range ( 0 , r - 13 + i ) :
            x { j } += 1;
    }
     else{
        for j in range ( i + 1 , i + 1 + r ) :
            x { j } += 1;
    }
    summ = 0;
    for (int j = 0; j < x.length; j++){
        if (j % 2 == 0) {
            summ += j;
        }
    }
     ans = max ( ans , summ );
System.out.println ( ans );
