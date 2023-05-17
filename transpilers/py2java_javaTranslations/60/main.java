import sys;
k , var p = map ( int , sys . stdin . readline ( ) . split ( ) );
var ans = 0;
var ans2 = 0;
var i = 1;
while (ans2 < k) {
    var s = str ( i );
    ans += int ( s + s { : : - 1 } );
    ans2 += 1;
    i += 1;
}
 System.out.println ( ans % p );
