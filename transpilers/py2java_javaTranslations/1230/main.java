import sys;
var input = sys . stdin . readline;
for _ in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    c , var d = 0 , 10 ** 9;
    for _ in range ( n ) :
        a , b = map ( int , input ( ) . split ( ) );
        if (a > c) {
            c = a;
        }
         if (b < d) {
            d = b;
        }
     if (c <= d) {
        System.out.println ( 0 );
    }
     else{
        System.out.println ( c - d );
    }
