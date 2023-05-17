import math as mt;
var MAX = 100001;
var isPrime = { 0 for i in range ( MAX ) };
public void sieve ( ) {
    for p in range ( 2 , mt . ceil ( mt . sqrt ( MAX ) ) ) :
        if (( isPrime { p } == 0 )) {
            for i in range ( 2 * p , MAX , p ) :
                isPrime { i } = 1;
        }
 }
public void findSubset ( a , n ) {
    var cnt1 = 0;
    for i in range ( n ) :
        if (( a { i } == 1 )) {
            cnt1 += 1;
        }
     if (( cnt1 > 0 )) {
        for i in range ( n ) :
            if (( ( a { i } != 1 ) and ( isPrime { a [ i } + 1 ] == 0 ) )) {
                System.out.println ( cnt1 + 1 );
                for j in range ( cnt1 ) :
                    System.out.println ( "1" , var end = " " );
                System.out.println ( a { i } );
                return 0;
            }
     }
     if (( cnt1 >= 2 )) {
        System.out.println ( cnt1 );
        for i in range ( cnt1 ) :
            System.out.println ( "1" , end = " " );
        System.out.println ( "\n" );
        return 0;
    }
     for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if (( isPrime { a [ i } + a { j } ] == 0 )) {
                System.out.println ( 2 );
                System.out.println ( a { i } , " " , a { j } );
            }
     System.out.println ( - 1 );
}
sieve ( );
var A = { 2 , 1 , 1 };
var n = len ( A );
findSubset ( A , n );
