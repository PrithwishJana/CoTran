import collections;
import heapq;
import sys;
import math;
import itertools;
import bisect;
import io.BytesIO , IOBase;
import os;
def values ( ) : return tuple ( map ( int , sys . stdin . readline ( ) . split ( ) ) );
def inlsts ( ) : return { int ( i ) for i in sys . stdin . readline ( ) . split ( ) };
def inp ( ) : return int ( sys . stdin . readline ( ) );
def instr ( ) : return sys . stdin . readline ( ) . strip ( );
def words ( ) : return { i for i in sys . stdin . readline ( ) . strip ( ) . split ( ) };
def chars ( ) : return { i for i in sys . stdin . readline ( ) . strip ( ) };
public void solve ( ) {
    var n = inp ( );
    var t = {} ; w = {};
    for i in range ( n ) :
        a , b = values ( );
        t . append ( a ) ; w . append ( b );
    sm = sum ( t );
    cnt = sum ( w );
    var dp = { - float ( 'inf' ) } * ( sm + 1 );
    dp { 0 } = 0;
    for i in range ( n ) :
        for j in range ( sm , t { i } - 1 , - 1 ) :
            dp { j } = max ( dp { j } , dp { j - t [ i } ] + w { i } );
    for i in range ( 1 , len ( dp ) ) :
        var rem = cnt - dp { i };
        if dp { i } > 0 and rem <= i : System.out.println ( i ) ; break;
}
if (var __name__ == "__main__") {
    solve ( );
}
 