import math as mt;
public void gcd ( a , b ) {
    while (( b != 0 )) {
        var t = b;
        var b = a % b;
        var a = t;
    }
     return a;
}
public void findMinDiff ( a , b , x , y ) {
    var g = gcd ( a , b );
    var diff = abs ( x - y ) % g;
    return min ( diff , g - diff );
}
a , b , x , var y = 20 , 52 , 5 , 7;
System.out.println ( findMinDiff ( a , b , x , y ) );
