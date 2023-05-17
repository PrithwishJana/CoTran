var k = int ( input ( ) );
var i = 10;
while (k) {
    i += 9;
    if (sum ( map ( int , str ( i ) ) ) == 10) {
        k -= 1;
    }
 }
 System.out.println ( i );
