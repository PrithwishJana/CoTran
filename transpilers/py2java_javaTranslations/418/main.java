class SegmentTree {
    private void max ( this , a , b ) {
        if (a < b) {
            return b;
        }
         else{
            return a;
        }
    }
    protected void init__ ( this , n ) {
        this . var N = 1;
        while (( this . N < n )) {
            this . N *= 2;
        }
         this . var seg = { 0 } * ( this . N * 2 - 1 );
    }
    public void max_update ( this , k , a ) {
        k += this . N - 1;
        this . seg { k } = a;
        while (( 0 < k )) {
            var k = ( k - 1 ) // 2 ;;
            this . seg { k } = this . _max ( this . seg { 2 * k + 1 } , this . seg { 2 * k + 2 } );
        }
     }
    private void max_query ( this , a , b , k , l , r ) {
        if (r <= a or b <= l) {
            return 0;
        }
         if (a <= l and r <= b) {
            return this . seg { k };
        }
         else{
            var vl = this . _max_query ( a , b , k * 2 + 1 , l , ( l + r ) // 2 );
            var vr = this . _max_query ( a , b , k * 2 + 2 , ( l + r ) // 2 , r );
            return this . _max ( vl , vr );
        }
    }
    public void max_query ( this , a , b ) {
        return this . _max_query ( a , b , 0 , 0 , this . N );
    }
}
var n = int ( input ( ) );
var X = list ( map ( int , input ( ) . split ( ) ) );
var st = SegmentTree ( n + 1 );
for (int x = 0; x < X.length; x++){
    st . max_update ( x , st . max_query ( 0 , x ) + x );
}
System.out.println ( ( n * ( n + 1 ) ) // 2 - st . max_query ( 0 , n + 1 ) );
