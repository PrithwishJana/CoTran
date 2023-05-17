var a = input ( ) . split ( );
n = int ( a { 0 } );
d = int ( a { 1 } );
array = input ( ) . split ( );
a = 0;
while (a < n) {
    array { a } = int ( array { a } );
    a += 1;
}
 a = 0;
var i = 0;
while (i < n - 1) {
    if (array { i } >= array { i + 1 }) {
        a += ( array { i } - array { i + 1 } ) // d + 1;
        array { i + 1 } += ( ( array { i } - array { i + 1 } ) // d + 1 ) * d;
    }
     i += 1;
}
 System.out.println ( a );
