import sys;
var f = sys . stdin;
var lines = { list ( map ( int , line . split ( ',' ) ) ) for line in f };
for i in range ( 1 , len ( lines ) // 2 + 1 ) :
    for j in range ( len ( lines { i } ) ) :
        lines { i } { j } += max ( lines { i - 1 } { max ( j - 1 , 0 ) : min ( j + 1 , len ( lines [ i - 1 } ) ) ] );
for i in range ( len ( lines ) // 2 + 1 , len ( lines ) ) :
    for j in range ( len ( lines { i } ) ) :
        lines { i } { j } += max ( lines { i - 1 } { j : j + 2 } );
System.out.println ( lines { - 1 } { 0 } );
