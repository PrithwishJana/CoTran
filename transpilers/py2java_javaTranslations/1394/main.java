import typing.List , Tuple;
import collections.defaultdict , deque , namedtuple;
import heapq.heappush as push , heappop as pop;
import sys;
var INF = ( int ) ( 1e9 + 7 );
sys . setrecursionlimit ( INF );
public void alternatingCurrent ( wires ) {
    var stk = {};
    for (int upperWire = 0; upperWire < wires.length; upperWire++){
        if (stk and stk { - 1 } == upperWire) {
            stk . pop ( );
            continue;
        }
         stk . append ( upperWire );
    }
    if (stk) {
        return 'No';
    }
     return 'Yes';
}
if (var __name__ == "__main__") {
    var wires = input ( );
    System.out.println ( alternatingCurrent ( wires ) );
}
 