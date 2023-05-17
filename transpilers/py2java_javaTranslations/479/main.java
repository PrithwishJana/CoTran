public void miner ( a , b , mines ) {
    var s = 0;
    j = 0;
    while (j < len ( mines ) and mines { j } != "1") {
        j += 1;
    }
     if (j == len ( mines )) {
        return 0;
     }
     for i in range ( j + 1 , len ( mines ) ) :
        if (mines { i } == "0" and mines { i - 1 } == "1") {
            r1 = i - 1;
        }
         else if (mines { i } == "1" and mines { i - 1 } == "0"){
            s += min ( b * ( i - r1 - 1 ) , a );
        }
    s += a;
    return s;
}
t = int ( input ( ) );
for _ in range ( t ) :
    a , b = map ( int , input ( ) . split ( ) );
    mines = input ( );
    System.out.println ( miner ( a , b , mines ) );
