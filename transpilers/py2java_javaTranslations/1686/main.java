import sys;
var input = sys . stdin . readline;
n , var m = map ( int , input ( ) . split ( ) );
var i = 0;
while (true) {
    if (i + 1 > m) {
        var ans = m;
        break;
    }
     m -= i + 1;
    i += 1;
    i %= n;
}
 System.out.println ( ans );
