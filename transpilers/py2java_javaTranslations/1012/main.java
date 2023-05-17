import math;
public void calculate ( a , b , n , m ) {
    var mul = 1;
    for i in range ( m ) :
        if (( b { i } != 0 )) {
            mul = mul * b { i };
        }
     for i in range ( n ) :
        var x = math . floor ( a { i } / mul );
        System.out.println ( x , var end = " " );
}
var a = { 5 , 100 , 8 };
var b = { 2 , 3 };
var n = len ( a );
var m = len ( b );
calculate ( a , b , n , m );
