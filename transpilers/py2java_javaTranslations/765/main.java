n , var k = map ( int , input ( ) . split ( ) );
var pw_list = { len ( input ( ) ) for _ in range ( n ) };
var pw = len ( input ( ) );
var p = sorted ( pw_list );
var head = p . index ( pw );
var tail = n - list ( reversed ( p ) ) . index ( pw ) - 1;
var worst_case = head + ( ( head ) // k ) * 5 + 1;
var best_case = tail + ( tail // k ) * 5 + 1;
System.out.println ( worst_case , best_case );
