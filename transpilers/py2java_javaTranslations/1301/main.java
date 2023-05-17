public void inv ( a , m ) {
    var m0 = m;
    var x0 = 0;
    x1 = 1;
    if (( m == 1 )) {
        return 0;
    }
     while (( a > 1 )) {
        q = a // m;
        t = m;
        m = a % m;
        a = t;
        t = x0;
        x0 = x1 - q * x0;
        var x1 = t;
    }
     if (( x1 < 0 )) {
        x1 = x1 + m0;
     }
     return x1;
}
public void findMinX ( num , rem , k ) {
    var prod = 1;
    for i in range ( 0 , k ) :
        prod = prod * num { i };
    var result = 0;
    for i in range ( 0 , k ) :
        pp = prod // num { i };
        result = result + rem { i } * inv ( pp , num { i } ) * pp;
    return result % prod;
}
var num = { 3 , 4 , 5 };
var rem = { 2 , 3 , 1 };
var k = len ( num );
System.out.println ( "x is " , findMinX ( num , rem , k ) );
