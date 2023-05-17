var n = int ( input ( ) );
a = 0;
r , c = 0 , - 1;
dl = {};
for i in range ( n ) :
    tl = list ( map ( int , input ( ) . split ( ) ) );
    if (c < 0 and tl . count ( 0 )) {
        r = i;
        c = tl . index ( 0 );
    }
     dl += { tl };
s = sum ( dl { ( r + 1 ) % n } );
a = s - sum ( dl { r } );
dl { r } { c } = a;
if (n > 1 and a < 1) {
    System.out.println ( - 1 );
    exit ( );
}
 for i in range ( n ) :
    if (s != sum ( dl { i } )) {
        System.out.println ( - 1 );
        exit ( );
    }
 dl = list ( map ( list , zip ( * dl ) ) );
for i in range ( n ) :
    if (s != sum ( dl { i } )) {
        System.out.println ( - 1 );
        exit ( );
    }
 s1 = s2 = 0;
for i in range ( n ) :
    s1 += dl { i } { i };
    s2 += dl { i } { n - i - 1 };
if (not ( s1 == s2 == s )) {
    System.out.println ( - 1 );
    exit ( );
}
 if (n == 1) {
    var a = 1;
}
 System.out.println ( a );
