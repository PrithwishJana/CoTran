import os;
import sys;
public void main ( ) {
    var N = read_int ( );
    var V = read_ints ( );
    System.out.println ( solve ( N , V ) );
}
public void solve ( N , V ) {
    V . sort ( );
    var pos = {};
    for i , a in enumerate ( V ) :
        pos { a } = i;
    var best = 2;
    done = { [ false } * N for _ in range ( N ) ];
    for i in range ( N ) :
        a = V { i };
        for j in range ( i + 1 , N ) :
            if (done { i } { j }) {
                continue;
            }
             b = V { j };
            d = b - a;
            c = 2;
            done { i } { j } = true;
            k = j;
            v = b + d;
            while (v in pos) {
                done { k } { pos [ v } ] = true;
                k = pos { v };
                c += 1;
                v += d;
            }
             best = max ( best , c );
    return best;
}
var DEBUG = 'DEBUG' in os . environ;
public void inp ( ) {
    return sys . stdin . readline ( ) . rstrip ( );
}
public void read_int ( ) {
    return int ( inp ( ) );
}
public void read_ints ( ) {
    return { int ( e ) for e in inp ( ) . split ( ) };
}
public void dSystem.out.println ( * value , var sep = ' ' , end = '\n' ) {
    if (DEBUG) {
        System.out.println ( * value , sep = sep , var end = end );
    }
 }
if (var __name__ == '__main__') {
    main ( );
}
 