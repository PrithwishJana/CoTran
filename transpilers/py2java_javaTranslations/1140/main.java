public void gcd ( a , b ) {
    if (( var a == 0 )) {
        return b;
    }
     return gcd ( b % a , a );
}
public void largestGCD1Subset ( A , n ) {
    var currentGCD = A { 0 } ;;
    for i in range ( 1 , n ) :
        currentGCD = gcd ( currentGCD , A { i } );
        if (( currentGCD == 1 )) {
            return n;
        }
     return 0;
}
var A = { 2 , 18 , 6 , 3 };
var n = len ( A );
System.out.println ( largestGCD1Subset ( A , n ) );
