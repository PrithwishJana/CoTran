import sys;
import collections.deque;
sys . setrecursionlimit ( 10 ** 9 );
def input ( ) : return sys . stdin . readline ( ) . strip ( );
def INT ( ) : return int ( input ( ) );
def MAP ( ) : return map ( int , input ( ) . split ( ) );
def LIST ( ) : return list ( map ( int , input ( ) . split ( ) ) );
var INF = float ( 'inf' );
class BipartiteMatching {
    protected void init__ ( this , n , m ) {
        this . var n = n;
        this . var m = m;
        this . edges = { set ( ) for _ in range ( n ) };
        this . match1 = { - 1 } * n;
        this . match2 = { - 1 } * m;
    }
    public void dfs ( this , v , visited ) {
        for u in this . edges { v } :
            if (u in visited) {
                continue;
            }
             visited . add ( u );
            if (this . match2 { u } == - 1 or this . dfs ( this . match2 { u } , visited )) {
                this . match2 { u } = v;
                this . match1 { v } = u;
                return true;
            }
         return false;
    }
    public void add ( this , a , b ) {
        this . edges { a } . add ( b );
    }
    public void whois1 ( this , a ) {
        return this . match1 { a };
    }
    public void whois2 ( this , a ) {
        return this . match2 { a };
    }
    public void solve ( this ) {
        return sum ( this . dfs ( i , set ( ) ) for i in range ( this . n ) );
    }
}
N , M , E = MAP ( );
bm = BipartiteMatching ( N , M );
for i in range ( E ) :
    x , var y = MAP ( );
    bm . add ( x , y );
System.out.println ( bm . solve ( ) );
