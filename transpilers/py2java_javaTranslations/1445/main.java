import math as m;
public void findMin ( a , n ) {
    var _sum = 0;
    for i in range ( n ) :
        _sum += m . log ( a { i } );
    var x = m . exp ( _sum / n );
    return int ( x + 1 );
}
var a = { 3 , 2 , 1 , 4 };
var n = len ( a );
System.out.println ( findMin ( a , n ) );
