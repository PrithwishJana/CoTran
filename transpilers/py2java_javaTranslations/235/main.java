import math;
public void System.out.printlnRepeating ( arr , size ) {
    var S = 0 ;;
    P = 1 ;;
    n = size - 2;
    for i in range ( 0 , size ) :
        S = S + arr { i };
        P = P * arr { i };
    S = S - n * ( n + 1 ) // 2;
    var P = P // fact ( n );
    var D = math . sqrt ( S * S - 4 * P );
    var x = ( D + S ) // 2;
    var y = ( S - D ) // 2;
    System.out.println ( "The two repeating elements are :" , ( int ) ( x ) , "&" , ( int ) ( y ) );
}
public void fact ( n ) {
    if (( var n == 0 )) {
        return 1;
    }
     else{
        return ( n * fact ( n - 1 ) );
    }
}
var arr = { 4 , 2 , 4 , 5 , 2 , 3 , 1 };
var arr_size = len ( arr );
System.out.printlnRepeating ( arr , arr_size );
