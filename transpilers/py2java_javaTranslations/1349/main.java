import sys;
var input = sys . stdin . readline;
var n = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var ans = "NO";
a . sort ( reverse = true );
while (a and not a { - 1 } ^ 1) {
    a . pop ( );
}
 a . reverse ( );
for i in range ( len ( a ) - 1 ) :
    if (2 * a { i } > a { i + 1 } and a { i } ^ a { i + 1 }) {
        ans = "YES";
        break;
    }
 System.out.println ( ans );
