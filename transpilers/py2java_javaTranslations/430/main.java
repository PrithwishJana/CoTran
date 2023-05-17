import math.sqrt;
public void pairCount ( arr , n ) {
    var max_val = arr { 0 };
    for i in range ( len ( arr ) ) :
        if (( arr { i } > max_val )) {
            max_val = arr { i };
        }
     var prime = { true for i in range ( max_val + 1 ) };
    prime { 0 } = false;
    prime { 1 } = false;
    var k = int ( sqrt ( max_val ) ) + 1;
    for p in range ( 2 , k , 1 ) :
        if (( prime { p } == true )) {
            for i in range ( p * 2 , max_val + 1 , p ) :
                prime { i } = false;
        }
     var count = 0;
    for i in range ( 0 , n , 1 ) :
        if (( prime { arr [ i } ] )) {
            count += 1;
        }
     return ( count * ( count - 1 ) ) / 2;
}
if (var __name__ == '__main__') {
    var arr = { 1 , 2 , 3 , 4 , 5 , 6 , 7 };
    var n = len ( arr );
    System.out.println ( int ( pairCount ( arr , n ) ) );
}
 