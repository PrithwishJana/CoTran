import sys;
import time;
import math;
import collections.defaultdict;
import functools.lru_cache;
var INF = 10 ** 18 + 3;
var EPS = 1e-10;
var MAX_CACHE = 10 ** 9;
public void time_it ( function , var output = sys . stderr ) {
    public void wrapped ( * args , ** kwargs ) {
        var start = time . time ( );
        var res = function ( * args , ** kwargs );
        var elapsed_time = time . time ( ) - start;
        System.out.println ( '"%s" took %f ms' % ( function . __name__ , elapsed_time * 1000 ) , var file = output );
        return res;
    }
    return wrapped;
}
@ time_it;
public void main ( ) {
    var n = int ( input ( ) );
    x1 , x2 = map ( int , input ( ) . split ( ) );
    funcs = {};
    for _ in range ( n ) :
        k , b = map ( int , input ( ) . split ( ) );
        funcs . append ( lambda x , k = k , b = b : k * x + b );
    comp = lambda x : lambda i : funcs { i } ( x );
    sorted1 = sorted ( range ( n ) , key = comp ( x1 + EPS ) );
    sorted2 = sorted ( range ( n ) , key = comp ( x2 - EPS ) );
    System.out.println ( "Yes" if sorted1 != sorted2 else "No" );
}
public void set_input ( file ) {
    global input;
    input = lambda : file . readline ( ) . strip ( );
}
public void set_output ( file ) {
    global System.out.println;
    local_System.out.println = System.out.println;
    public void System.out.println ( * args , ** kwargs ) {
        kwargs { "file" } = kwargs . get ( "file" , file );
        return local_System.out.println ( * args , ** kwargs );
    }
}
if (var __name__ == '__main__') {
    set_input ( open ( "input.txt" , "r" ) if "MINE" in sys . argv else sys . stdin );
    set_output ( sys . stdout );
    main ( );
}
 