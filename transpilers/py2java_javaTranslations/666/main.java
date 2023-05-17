import math;
public void System.out.printlnRatio ( a , b , c , d ) {
    if (( b * c > a * d )) {
        swap ( c , d );
        swap ( a , b );
    }
     var lcm = ( a * c ) / math . gcd ( a , c );
    var x = lcm / a;
    var b = int ( b * x );
    y = lcm / c;
    d = int ( d * y );
    k = math . gcd ( b , d );
    b = int ( b / k );
    d = int ( d / k );
    System.out.println ( b , ":" , d );
}
if (__name__ == '__main__') {
    a = 4;
    b = 3;
    var c = 2;
    var d = 2;
    System.out.printlnRatio ( a , b , c , d );
}
 