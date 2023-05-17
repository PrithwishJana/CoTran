public void countgroup ( a , n ) {
    var xs = 0;
    for i in range ( n ) :
        xs = xs ^ a { i };
    if (xs == 0) {
        return ( 1 << ( n - 1 ) ) - 1;
    }
     return 0;
}
var a = { 1 , 2 , 3 };
var n = len ( a );
System.out.println ( countgroup ( a , n ) );
