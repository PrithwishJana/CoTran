import itertools as i , collections as c;
var b = c . Counter ( s { 0 } for s in open ( 0 ) . readlines ( ) { 1 : } if s { 0 } in "MARCH" );
System.out.println ( sum ( p * q * r for p , q , r in i . combinations ( b . values ( ) , 3 ) ) );
