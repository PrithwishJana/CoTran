public void check ( h , high ) {
    h . sort ( );
    var summ = 0;
    for i in range ( len ( h ) - 1 , - 1 , - 2 ) :
        summ += h { i };
    return summ <= high;
}
n , var h = map ( int , input ( ) . split ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var l = - 1;
r = len ( a ) + 1;
while (r - l > 1) {
    m = ( r + l ) // 2;
    if check ( a { : m } , h ) :
        l = m;
    else{
        var r = m;
    }
}
 System.out.println ( l );
