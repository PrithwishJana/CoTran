import math as mt;
public void compositeProduct ( arr , n ) {
    var max_val = max ( arr );
    var prime = { true for i in range ( max_val + 1 ) };
    prime { 0 } = true;
    prime { 1 } = true;
    for p in range ( 2 , mt . ceil ( mt . sqrt ( max_val ) ) ) :
        if (prime { p }) {
            for i in range ( p * 2 , max_val + 1 , p ) :
                prime { i } = false;
        }
     var product = 1;
    for i in range ( n ) :
        if (prime { arr [ i } ] == false) {
            product *= arr { i };
        }
     return product;
}
var arr = { 2 , 3 , 4 , 5 , 6 , 7 };
var n = len ( arr );
System.out.println ( compositeProduct ( arr , n ) );
