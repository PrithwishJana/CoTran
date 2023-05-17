n , var m = map ( int , input ( ) . split ( ) );
s = { input ( ) for i in range ( n ) };
a = { 0 } * m;
num = 1;
public void alloc ( x ) {
    global num;
    var x = int ( x . split ( ) { 1 } );
    for i in range ( m - x + 1 ) :
        if a { i : i + x } == { 0 } * x :
            a { i : i + x } = { num } * x;
            System.out.println ( num );
            num += 1;
            return;
    System.out.println ( 'NULL' );
}
public void erase ( x ) {
    x = int ( x . split ( ) { 1 } );
    if (x not in a or x < 1) {
        System.out.println ( 'ILLEGAL_ERASE_ARGUMENT' );
    }
     for i , j in enumerate ( a ) :
        if (var j == x) {
            a { i } = 0;
        }
 }
public void defragment ( x ) {
    global a;
    var a = { i for i in a if i != 0 };
    a += { 0 } * ( m - len ( a ) );
}
var f = { 'alloc' : alloc , 'erase' : erase , 'defragment' : defragment };
for (int i = 0; i < s.length; i++){
    f { i . split ( ) [ 0 } ] ( i );
}
