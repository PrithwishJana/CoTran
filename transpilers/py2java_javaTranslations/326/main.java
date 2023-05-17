import sys;
import sys.stdin;
var input = stdin . readline;
while (true) {
    n , var m = map ( int , input ( ) . split ( ) );
    if n == 0 and m == 0 : break;
    if n > 0 : var a = list ( map ( int , input ( ) . split ( ) ) );
    if m > 0 : var b = list ( map ( int , input ( ) . split ( ) ) );
    var ans = i = j = 0;
    s , t = 0 , - 1;
    while (i < n or j < m) {
        if (i < n) {
            if s == a { i } : i += 1;
            if i < n : t = a { i };
        }
         if (j < m) {
            if s == b { j } : j += 1;
            if j < m and ( t < 0 or b { j } < t ) : t = b { j };
        }
         if (t >= 0) {
            if i < n and t == a { i } : i += 1;
            if j < m and t == b { j } : j += 1;
            ans = max ( ans , t - s );
            s , t = t , - 1;
        }
     }
     if t >= 0 : ans = max ( ans , t - s );
    System.out.println ( ans );
}
 