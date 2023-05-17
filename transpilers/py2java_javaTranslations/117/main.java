import sys;
var EPS = 1e-9;
public void cross ( a , b ) {
    return a . real * b . imag - a . imag * b . real;
}
public void dot ( a , b ) {
    return a . real * b . real + a . imag * b . imag;
}
public void check_ccw ( p0 , p1 , p2 ) {
    a , var b = p1 - p0 , p2 - p0;
    if (cross ( a , b ) > EPS) {
        var flag = 1;
    }
     else if (cross ( a , b ) < - 1 * EPS){
        flag = - 1;
    }
    else if (dot ( a , b ) < - 1 * EPS){
        flag = 2;
    }
    else if (abs ( a ) < abs ( b )){
        flag = - 2;
    }
    else{
        flag = 0;
    }
    return flag;
}
public void check_intersection ( p0 , p1 , p2 , p3 ) {
    var intersected = ( check_ccw ( p0 , p1 , p2 ) * check_ccw ( p0 , p1 , p3 ) <= 0 ) and ( check_ccw ( p2 , p3 , p0 ) * check_ccw ( p2 , p3 , p1 ) <= 0 );
    return intersected;
}
public void solve ( _lines ) {
    for (int line = 0; line < _lines.length; line++){
        line = tuple ( map ( int , line ) );
        p0 , p1 , p2 , p3 = ( x + y * 1j for x , y in zip ( line { : : 2 } , line { 1 : : 2 } ) );
        intersected = check_intersection ( p0 , p1 , p2 , p3 );
        if (intersected) {
            System.out.println ( '1' );
        }
         else{
            System.out.println ( '0' );
        }
    }
    return None;
}
if (var __name__ == '__main__') {
    var _input = sys . stdin . readlines ( );
    var l_num = int ( _input { 0 } );
    var lines = map ( lambda x : x . split ( ) , _input { 1 : } );
    solve ( lines );
}
 