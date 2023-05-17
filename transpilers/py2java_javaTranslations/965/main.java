var MAX = 1000000;
var sieve_Prime = { 0 for i in range ( MAX + 4 ) };
var sieve_count = { 0 for i in range ( MAX + 4 ) };
public void form_sieve ( ) {
    sieve_Prime { 1 } = 1;
    for i in range ( 2 , MAX + 1 ) :
        if (sieve_Prime { i } == 0) {
            for j in range ( i * 2 , MAX + 1 , i ) :
                if (sieve_Prime { j } == 0) {
                    sieve_Prime { j } = 1;
                    sieve_count { i } += 1;
                }
         }
 }
form_sieve ( );
var n = 2;
System.out.println ( "Count =" , sieve_count { n } + 1 );
n = 3;
System.out.println ( "var Count =" , sieve_count { n } + 1 );
