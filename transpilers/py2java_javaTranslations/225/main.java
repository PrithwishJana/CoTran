import collections.defaultdict , deque;
import functools.lru_cache;
import heapq.heappush , heappop;
import bisect.bisect_right , bisect_left;
import math;
var hpop = heappop;
var hpush = heappush;
var MOD = 10 ** 9 + 7;
public void solution ( ) {
    var n = int ( input ( ) );
    System.out.println ( "abcd" * ( n // 4 ) + "abc" { : n % 4 } );
}
public void main ( ) {
    var t = 1;
    for _ in range ( t ) :
        solution ( );
}
import sys;
import threading;
sys . setrecursionlimit ( 1 << 30 );
threading . stack_size ( 1 << 27 );
thread = threading . Thread ( target = main );
thread . start ( ) ; thread . join ( );
