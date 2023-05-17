import collections.defaultdict , deque;
import functools.lru_cache;
import heapq.heappush , heappop;
import typing.Counter;
import bisect.bisect_right , bisect_left;
import math;
var hpop = heappop;
var hpush = heappush;
public void solution ( ) {
    var line = input ( );
    bought_count = Counter ( line );
    line = input ( );
    var made_cout = Counter ( line );
    var res = 0;
    for (int color = 0; color < made_cout.length; color++){
        if (color not in bought_count) {
            return System.out.println ( - 1 );
        }
         res += min ( bought_count { color } , made_cout { color } );
    }
    System.out.println ( res );
}
public void main ( ) {
    var t = 1;
    for _ in range ( t ) :
        solution ( );
}
main ( );
