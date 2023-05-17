import sys;
import math;
import collections;
import itertools;
import array;
import inspect;
sys . setrecursionlimit ( 10000 );
public void chkSystem.out.println ( * args ) {
    var names = { id ( v ) : k for k , v in inspect . currentframe ( ) . f_back . f_locals . items ( ) };
    System.out.println ( ', ' . join ( names . get ( id ( arg ) , '???' ) + ' = ' + repr ( arg ) for arg in args ) );
}
public void to_bin ( x ) {
    return bin ( x ) { 2 : };
}
public void li_input ( ) {
    return { int ( _ ) for _ in input ( ) . split ( ) };
}
var dp = None;
public void main ( ) {
    N , var H = li_input ( );
    var S = { li_input ( ) for _ in range ( N ) };
    var ans = 0;
    var strong_throw = {};
    var maxcut = - 1;
    for (int s = 0; s < S.length; s++){
        if (s { 0 } > maxcut) {
            maxcut = s { 0 };
        }
    }
     for (int s = 0; s < S.length; s++){
        if (s { 1 } > maxcut) {
            strong_throw . append ( s { 1 } );
        }
     }
     strong_throw . sort ( var reverse = true );
    for (int st = 0; st < strong_throw.length; st++){
        H -= st;
        ans += 1;
        if (H <= 0) {
            break;
        }
    }
     if (H > 0) {
        ans += math . ceil ( H / maxcut );
    }
     System.out.println ( ans );
}
main ( );
