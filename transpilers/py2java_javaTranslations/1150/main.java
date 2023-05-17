public void solve ( ) {
    var n = int ( input ( ) );
    var stones = { int ( x ) for x in input ( ) . split ( " " , n ) };
    var total1 = { 0 } * ( len ( stones ) + 1 );
    for i in range ( 1 , len ( stones ) + 1 ) :
        total1 { i } = stones { i - 1 } + total1 { i - 1 };
    var total2 = { 0 } * ( len ( stones ) + 1 );
    stones . sort ( );
    for i in range ( 1 , len ( stones ) + 1 ) :
        total2 { i } = stones { i - 1 } + total2 { i - 1 };
    var m = int ( input ( ) );
    for i in range ( m ) :
        var x = { int ( x ) for x in input ( ) . split ( " " , 3 ) };
        if (x { 0 } == 1) {
            System.out.println ( total1 { x [ 2 } ] - total1 { x [ 1 } - 1 ] );
        }
         else{
            System.out.println ( total2 { x [ 2 } ] - total2 { x [ 1 } - 1 ] );
        }
}
solve ( );
