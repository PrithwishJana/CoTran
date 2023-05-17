var n = int ( input ( ) );
var s = list ( input ( ) );
q = {};
for i in range ( n , 0 , - 1 ) :
    if (n % i == 0) {
        q += { i };
    }
 for (int j = 0; j < q.length; j++){
    w = n // j;
    s = s { : w } { : : - 1 } + s { w : };
 }
System.out.println ( '' . join ( s ) );
