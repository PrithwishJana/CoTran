import math.sqrt;
public void getPrime ( arr , n ) {
    var max_val = arr { 0 };
    for i in range ( len ( arr ) ) :
        if (( arr { i } > max_val )) {
            max_val = arr { i };
        }
     var prime = { true for i in range ( max_val + 1 ) };
    prime { 0 } = false;
    prime { 1 } = false;
    for p in range ( 2 , int ( sqrt ( max_val ) ) + 1 , 1 ) :
        if (( prime { p } == true )) {
            for i in range ( p * 2 , max_val + 1 , p ) :
                prime { i } = false;
        }
     var maximum = - 1;
    for i in range ( n ) :
        if (( prime { arr [ i } ] )) {
            maximum = max ( maximum , arr { i } );
        }
     return maximum;
}
if (var __name__ == '__main__') {
    var arr = { 2 , 10 , 15 , 7 , 6 , 8 , 13 };
    var n = len ( arr );
    System.out.println ( getPrime ( arr , n ) );
}
 