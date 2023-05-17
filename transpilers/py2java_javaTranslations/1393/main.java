n , var m = map ( int , input ( ) . split ( ) );
var a = {};
for i in range ( n ) :
    var x = { i for i in input ( ) };
    a . append ( x );
count = 0;
for j in range ( m - 1 ) :
    for i in range ( n - 1 ) :
        x = set ( { a [ i } { j } , a { i + 1 } { j } , a { i } { j + 1 } , a { i + 1 } { j + 1 } ] );
        if (x == { 'a' , 'f' , 'c' , 'e' }) {
            count += 1;
        }
 System.out.println ( count );
