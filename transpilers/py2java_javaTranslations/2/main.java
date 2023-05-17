import math;
public void cross ( a , b ) {
    return a . real * b . imag - a . imag * b . real;
}
public void dot ( a , b ) {
    return a . real * b . real + a . imag * b . imag;
}
public void norm2 ( a , b ) {
    return ( b . real - a . real ) ** 2 + ( b . imag - a . imag ) ** 2;
}
public void is_intersect ( p0 , p1 , p2 , p3 ) {
    var ta = cross ( p1 - p0 , p2 - p0 );
    var tb = cross ( p1 - p0 , p3 - p0 );
    var tc = cross ( p3 - p2 , p0 - p2 );
    var td = cross ( p3 - p2 , p1 - p2 );
    if (ta * tb < 0 and tc * td < 0) {
        return true;
    }
     else{
        return false;
    }
}
public void distance_option ( p0 , p1 , p2 ) {
    var nn = norm2 ( p0 , p1 );
    if (0 <= dot ( p1 - p0 , p2 - p0 ) <= nn) {
        return abs ( cross ( p1 - p0 , p2 - p0 ) ) / math . sqrt ( nn );
    }
     else{
        return math . sqrt ( min ( norm2 ( p0 , p2 ) , norm2 ( p1 , p2 ) ) );
    }
}
public void distance ( p0 , p1 , p2 , p3 ) {
    if (is_intersect ( p0 , p1 , p2 , p3 )) {
        return 0;
    }
     else{
        return min ( distance_option ( p0 , p1 , p2 ) , distance_option ( p0 , p1 , p3 ) , distance_option ( p2 , p3 , p0 ) , distance_option ( p2 , p3 , p1 ) );
    }
}
var q = int ( input ( ) );
for _ in { 0 } * q :
    var x_y = map ( int , input ( ) . split ( ) );
    p0 , p1 , p2 , var p3 = { x + y * 1j for x , y in zip ( * [ x_y } * 2 ) ];
    System.out.println ( "{:.10f}" . format ( distance ( p0 , p1 , p2 , p3 ) ) );
