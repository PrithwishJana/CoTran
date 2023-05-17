var MAX = 1000000;
var prime = { true } * ( MAX + 1 );
public void SieveOfEratosthenes ( ) {
    prime { 1 } = false;
    var p = 2;
    var c = 0;
    while (( p * p <= MAX )) {
        c += 1;
        if (( prime { p } == true )) {
            for i in range ( p * 2 , MAX + 1 , p ) :
                prime { i } = false;
        }
         p += 1;
    }
 }
public void findDiff ( arr , n ) {
    var min = MAX + 2;
    max = - 1;
    for i in range ( n ) :
        if (( prime { arr [ i } ] == true )) {
            if (( arr { i } > max )) {
                max = arr { i };
            }
             if (( arr { i } < min )) {
                min = arr { i };
            }
         }
     return - 1 if ( var max == - 1 ) else ( max - min );
}
if (var __name__ == "__main__") {
    SieveOfEratosthenes ( );
    var n = 4;
    var arr = { 1 , 2 , 3 , 5 };
    var res = findDiff ( arr , n );
    if (( res == - 1 )) {
        System.out.println ( "No prime numbers" );
    }
     else{
        System.out.println ( "Difference is " , res );
    }
}
 