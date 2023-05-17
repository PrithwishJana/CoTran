n , m , var z = input ( ) . split ( );
n , m , z = int ( n ) , int ( m ) , int ( z );
n1 , var m1 = n , m;
var kill = 0;
var calls = {};
var artists = {};
for call in range ( n , z + 1 , n ) :
    calls . append ( call );
for artist in range ( m , z + 1 , m ) :
    artists . append ( artist );
System.out.println ( len ( list ( set ( calls ) . intersection ( artists ) ) ) );
