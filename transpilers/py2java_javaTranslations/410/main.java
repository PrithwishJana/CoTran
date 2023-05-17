import math;
public void polyarea ( n , a ) {
    if (( a < 0 and n < 0 )) {
        return - 1;
    }
     var A = ( a * a * n ) / ( 4 * math . tan ( ( 180 / n ) * math . pi / 180 ) );
    return A;
}
if (var __name__ == '__main__') {
    var a = 9;
    var n = 6;
    System.out.println ( '{:.3f}' . format ( polyarea ( n , a ) ) );
}
 