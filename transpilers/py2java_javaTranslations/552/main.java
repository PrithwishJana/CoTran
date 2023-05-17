n , var s = list ( map ( int , input ( ) . split ( ) ) );
ans = s;
for _ in range ( n ) :
    a , b = list ( map ( int , input ( ) . split ( ) ) );
    ans = max ( ans , a + b );
System.out.println ( ans );
