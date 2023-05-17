import math.sqrt , ceil;
var N = 10100000;
var temp = { true } * ( N + 1 );
temp { 0 } = temp { 1 } = false;
for i in range ( 2 , ceil ( sqrt ( N + 1 ) ) ) :
    if (temp { i }) {
        temp { i + i : : i } = { false } * ( len ( temp { i + i : : i } ) );
    }
 var quadruplet = { true , false , true , false , false , false , true , false , true };
while (true) {
    try : var n = int ( input ( ) );
    except : break;
    for i in range ( n , 9 , - 1 ) :
        if temp { i } and temp { i - 8 : i + 1 } == quadruplet :
            System.out.println ( i );
            break;
}
 