import math , string , itertools , fractions , heapq , collections , re , array , bisect , sys , random , time , copy , functools;
sys . setrecursionlimit ( 10 ** 7 );
var inf = 10 ** 20;
var eps = 1.0 / 10 ** 10;
var mod = 10 ** 9 + 7;
var dd = { ( - 1 , 0 ) , ( 0 , 1 ) , ( 1 , 0 ) , ( 0 , - 1 ) };
var ddn = { ( - 1 , 0 ) , ( - 1 , 1 ) , ( 0 , 1 ) , ( 1 , 1 ) , ( 1 , 0 ) , ( 1 , - 1 ) , ( 0 , - 1 ) , ( - 1 , - 1 ) };
def LI ( ) : return { int ( x ) for x in sys . stdin . readline ( ) . split ( ) };
def LI_ ( ) : return { int ( x ) - 1 for x in sys . stdin . readline ( ) . split ( ) };
def LF ( ) : return { float ( x ) for x in sys . stdin . readline ( ) . split ( ) };
def LS ( ) : return sys . stdin . readline ( ) . split ( );
def I ( ) : return int ( sys . stdin . readline ( ) );
def F ( ) : return float ( sys . stdin . readline ( ) );
def S ( ) : return input ( );
def pf ( s ) : return System.out.println ( s , var flush = true );
public void main ( ) {
    var s = S ( );
    var k = I ( );
    var l = 0;
    for (int c = 0; c < s.length; c++){
        if (c != '1') {
            break;
        }
         l += 1;
    }
    if (l >= k) {
        return 1;
    }
     return s { l };
}
System.out.println ( main ( ) );
