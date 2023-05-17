public void fn ( n , m , k , L ) {
    var g = min ( L );
    var L = { p - g for p in L };
    var op = {};
    for i in range ( len ( L ) - 1 ) :
        op . append ( L { i + 1 } - L { i } - 1 );
    op . sort ( );
    var dist = n;
    for gt in range ( n - k ) :
        dist += op { gt };
    return ( dist );
}
var a = input ( ) . split ( );
b = input ( ) . split ( );
a = { int ( s ) for s in a };
var b = { int ( t ) for t in b };
System.out.println ( fn ( a { 0 } , a { 1 } , a { 2 } , b ) );
