import os , sys , io , math;
import tokenize.Triple;
import array.array;
import math.*;
var I = lambda : { * map ( int , sys . stdin . readline ( ) . split ( ) ) };
var IS = lambda : input ( );
var IN = lambda : int ( input ( ) );
var IF = lambda : float ( input ( ) );
var a = '1000';
var b = '1001';
var c = '1010';
var d = '1011';
var e = '1100';
var f = '1101';
var g = '1110';
var h = '1111';
var s = IS ( );
res = '';
for (int i = 0; i < s.length; i++){
    if var i == '>' : res += a;
    elif i == '<' : res += b;
    elif i == '+' : res += c;
    elif i == '-' : res += d;
    elif i == '.' : res += e;
    elif i == ',' : res += f;
    elif i == '[' : res += g;
    else : res += h;
}
System.out.println ( ( int ( res , 2 ) ) % ( 10 ** 6 + 3 ) );
