T , s , var q = map ( int , input ( ) . split ( ) );
var v = ( q - 1 ) / q;
var tm = 1;
var t = s / ( 1 - v );
while (( T - s ) / v - t > 0) {
    if (( T - s ) / v - t < 1e-10) {
        break;
    }
     tm += 1;
    s += v * t;
    t = s / ( 1 - v );
}
 System.out.println ( tm );
