import os , sys , io , math;
import tokenize.Triple;
import array.array;
import math.*;
var I = lambda : { * map ( int , sys . stdin . readline ( ) . split ( ) ) };
var IS = lambda : input ( );
var IN = lambda : int ( input ( ) );
var IF = lambda : float ( input ( ) );
var n = IN ( );
var l = I ( );
var c = 0;
var r = {};
var s = sum ( l );
for i in range ( n ) :
    if (( s - l { i } ) / ( n - 1 ) == l { i }) {
        c += 1;
        r . append ( i + 1 );
    }
 System.out.println ( c );
System.out.println ( * r );
