import math as mt;
public void countNumbersWith4 ( n ) {
    if (( n < 4 )) {
        return 0;
    }
     var d = int ( mt . log10 ( n ) );
    a = { 1 for i in range ( d + 1 ) };
    a { 0 } = 0;
    if (len ( a ) > 1) {
        a { 1 } = 1;
    }
     for i in range ( 2 , d + 1 ) :
        a { i } = a { i - 1 } * 9 + mt . ceil ( pow ( 10 , i - 1 ) );
    p = mt . ceil ( pow ( 10 , d ) );
    msd = n // p;
    if (( msd == 4 )) {
        return ( msd ) * a { d } + ( n % p ) + 1;
    }
     if (( msd > 4 )) {
        return ( ( msd - 1 ) * a { d } + p + countNumbersWith4 ( n % p ) );
    }
     return ( msd ) * a { d } + countNumbersWith4 ( n % p );
}
var n = 328;
System.out.println ( "Count of numbers from 1 to" , n , "that have 4 as a digit is" , countNumbersWith4 ( n ) );
