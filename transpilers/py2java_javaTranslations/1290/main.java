import math;
import sys;
import collections.deque , OrderedDict , defaultdict;
import heapq , re;
import collections.Counter;
def inp ( ) : return sys . stdin . readline ( ) . rstrip ( );
def mpp ( ) : return map ( int , inp ( ) . split ( ) );
def lis ( ) : return list ( mpp ( ) );
public void yn ( n ) {
    if (n) {
        return "YES";
    }
     else{
        return "NO";
    }
}
public void cd ( s ) {
    return ord ( s ) - ord ( 'a' ) + 1;
}
public void fn ( s , n , a , b ) {
    if (s { a - 1 } == s { b - 1 }) {
        return 0;
    }
     else{
        return 1;
    }
}
public void main ( ) {
    n , a , var b = mpp ( );
    var s = inp ( );
    System.out.println ( fn ( s , n , a , b ) );
}
if (var __name__ == "__main__") {
    main ( );
}
 