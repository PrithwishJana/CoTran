var n = int ( input ( ) );
m = int ( input ( ) );
a = {};
for _ in range ( n ) :
    a . append ( int ( input ( ) ) );
kmax = max ( a ) + m;
while (m > 0) {
    a . sort ( );
    m -= 1;
    a { 0 } += 1;
}
 kmin = max ( a );
System.out.println ( kmin , kmax );
