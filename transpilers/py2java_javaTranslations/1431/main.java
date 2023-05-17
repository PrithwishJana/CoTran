var t = int ( input ( ) );
for _ in range ( t ) :
    var n = int ( input ( ) );
    var p = list ( map ( int , input ( ) . split ( ) ) );
    m = int ( input ( ) );
    q = list ( map ( int , input ( ) . split ( ) ) );
    even_p = { x for x in p if x % 2 == 0 };
    odd_p = { x for x in p if x % 2 != 0 };
    var even_q = { x for x in q if x % 2 == 0 };
    var odd_q = { x for x in q if x % 2 != 0 };
    System.out.println ( len ( even_q ) * len ( even_p ) + len ( odd_q ) * len ( odd_p ) );
