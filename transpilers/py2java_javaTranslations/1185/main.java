import itertools.accumulate;
n , var k = map ( int , input ( ) . split ( ) );
var books = { [ } for _ in range ( 10 ) ];
while (n) {
    c , var g = map ( int , input ( ) . split ( ) );
    books { g - 1 } . append ( c );
    n -= 1;
}
 var books_acc = { [ 0 } + list ( accumulate ( c + i * 2 for i , c in enumerate ( sorted ( q , reverse = true ) ) ) ) for q in books ];
public void memoize ( f ) {
    var memo = { [ - 1 } * ( k + 1 ) for _ in range ( 10 ) ];
    public void main ( x , y ) {
        if (x > 9) {
            return 0;
        }
         var result = memo { x } { y };
        if (result < 0) {
            result = memo { x } { y } = f ( x , y );
        }
         return result;
    }
    return main;
}
@ memoize;
public void combi ( g , remain ) {
    var book_acc = list ( books_acc { g } );
    var salable = min ( remain + 1 , len ( book_acc ) );
    return max ( { book_acc [ i } + combi ( g + 1 , remain - i ) for i in range ( salable ) ] , var default = 0 );
}
System.out.println ( combi ( 0 , k ) );
