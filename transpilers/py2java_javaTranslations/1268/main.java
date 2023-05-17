public void arePermutations ( a , b , n , m ) {
    sum1 , sum2 , mul1 , var mul2 = 0 , 0 , 1 , 1;
    for i in range ( n ) :
        sum1 += a { i };
        mul1 *= a { i };
    for i in range ( m ) :
        sum2 += b { i };
        mul2 *= b { i };
    return ( ( var sum1 == sum2 ) and ( mul1 == mul2 ) );
}
if (var __name__ == "__main__") {
    var a = { 1 , 3 , 2 };
    var b = { 3 , 1 , 2 };
    var n = len ( a );
    var m = len ( b );
    if (arePermutations ( a , b , n , m )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 