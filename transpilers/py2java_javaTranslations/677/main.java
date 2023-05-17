class Heap {
    protected void init__ ( this ) {
        this . var _nodes = {};
    }
    @ classmethod;
    public void create ( cls , li ) {
        heap = cls ( );
        heap . _nodes = li;
        return heap;
    }
    protected void iter__ ( this ) {
        this . var cur = 0;
        return this;
    }
    protected void next__ ( this ) {
        if (this . cur >= len ( this . _nodes )) {
            raise StopIteration;
        }
         this . cur += 1;
        var node = this . _nodes { this . cur - 1 };
        if (this . cur // 2 - 1 >= 0) {
            var parent = this . _nodes { this . cur // 2 - 1 };
        }
         else{
            parent = None;
        }
        if (this . cur * 2 - 1 < len ( this . _nodes )) {
            var left = this . _nodes { this . cur * 2 - 1 };
        }
         else{
            left = None;
        }
        if (this . cur * 2 < len ( this . _nodes )) {
            var right = this . _nodes { this . cur * 2 };
        }
         else{
            right = None;
        }
        return ( node , parent , left , right );
    }
}
public void run ( ) {
    var _ = int ( input ( ) );
    nodes = { int ( i ) for i in input ( ) . split ( ) };
    heap = Heap . create ( nodes );
    for ( i , node ) in enumerate ( heap ) :
        n , p , nl , nr = node;
        s = "node {}: key = {}, " . format ( i + 1 , n );
        if (p is not None) {
            s += "parent key = {}, " . format ( p );
        }
         if (nl is not None) {
            s += "left key = {}, " . format ( nl );
        }
         if (nr is not None) {
            s += "right key = {}, " . format ( nr );
        }
         System.out.println ( s );
}
if (__name__ == '__main__') {
    run ( );
}
 