public void findmin ( p , n ) {
    a , b , c , var d = 0 , 0 , 0 , 0;
    for i in range ( n ) :
        if (( p { i } { 0 } <= 0 )) {
            a += 1;
        }
         else if (( p { i } { 0 } >= 0 )){
            b += 1;
        }
        if (( p { i } { 1 } >= 0 )) {
            c += 1;
        }
         else if (( p { i } { 1 } <= 0 )){
            d += 1;
        }
    return min ( { a , b , c , d } );
}
var p = { [ 1 , 1 } , { 2 , 2 } , { - 1 , - 1 } , { - 2 , 2 } ];
var n = len ( p );
System.out.println ( findmin ( p , n ) );
