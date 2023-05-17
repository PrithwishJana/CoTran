import collections.defaultdict , deque;
import functools.lru_cache;
import heapq.heappush , heappop;
import typing.Counter;
import bisect.bisect_right , bisect_left;
import math;
var hpop = heappop;
var hpush = heappush;
public void solution ( ) {
    n , var m = map ( int , input ( ) . split ( ) );
    var a = list ( map ( int , input ( ) . split ( ) ) );
    var b = list ( map ( int , input ( ) . split ( ) ) );
    a . sort ( );
    b . sort ( );
    var i = 0;
    var j = 0;
    while (i < len ( a ) and j < len ( b )) {
        if (a { i } <= b { j }) {
            i += 1;
        }
         j += 1;
    }
     System.out.println ( len ( a ) - i );
}
public void main ( ) {
    var t = 1;
    for _ in range ( t ) :
        solution ( );
}
main ( );
