import collections.defaultdict , deque;
import sys , heapq , bisect , math , itertools , string , queue , datetime;
sys . setrecursionlimit ( 10 ** 8 );
var INF = float ( 'inf' );
var mod = 10 ** 9 + 7;
def inpl ( ) : return list ( map ( int , input ( ) . split ( ) ) );
def inpls ( ) : return list ( input ( ) . split ( ) );
var N = int ( input ( ) );
public void dsum ( x ) {
    return sum ( map ( int , list ( str ( x ) ) ) );
}
var ans = INF;
for a in range ( 1 , N ) :
    b = N - a;
    ans = min ( ans , dsum ( a ) + dsum ( b ) );
System.out.println ( ans );
