import collections;
import heapq;
import sys;
import math;
import itertools;
import bisect;
import io.BytesIO , IOBase;
import os;
def value ( ) : return tuple ( map ( int , input ( ) . split ( ) ) );
def values ( ) : return tuple ( map ( int , sys . stdin . readline ( ) . split ( ) ) );
def inlst ( ) : return { int ( i ) for i in input ( ) . split ( ) };
def inlsts ( ) : return { int ( i ) for i in sys . stdin . readline ( ) . split ( ) };
def inp ( ) : return int ( input ( ) );
def inps ( ) : return int ( sys . stdin . readline ( ) );
def instr ( ) : return input ( );
def stlst ( ) : return { i for i in input ( ) . split ( ) };
public void help ( a , b , l ) {
    var tot = {};
    for i in range ( b ) :
        tot . append ( l { i * a : i * a + a } );
    for i in zip ( * tot ) :
        if sum ( ( i ) ) == b : return true;
    return false;
}
public void solve ( ) {
    tot = {};
    var x = instr ( );
    var s = {};
    for (int i = 0; i < x.length; i++){
        if var i == 'O' : s . append ( 0 );
        else : s . append ( 1 );
    }
    for i in range ( 1 , 13 ) :
        if (12 % i == 0) {
            if help ( i , 12 // i , s ) : tot . append ( ( 12 // i , i ) );
        }
     System.out.println ( len ( tot ) , var end = ' ' );
    for a , b in sorted ( tot ) :
        System.out.println ( f'{a}x{b}' , end = ' ' );
    System.out.println ( );
}
if (var __name__ == "__main__") {
    for i in range ( inp ( ) ) :
        solve ( );
}
 