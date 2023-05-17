import os , sys , io , math;
import array.array;
import math.*;
var I = lambda : { * map ( int , sys . stdin . readline ( ) . split ( ) ) };
var IS = lambda : input ( );
var IN = lambda : int ( input ( ) );
var IF = lambda : float ( input ( ) );
var n = IN ( );
var l = I ( );
var f = 1;
l . sort ( );
var c = 0;
for (int i = 0; i < l.length; i++){
    if i > c : c += 1;
}
System.out.println ( c + 1 );
