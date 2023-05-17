public void solve ( n , nums ) {
    var maxIndex = nums . index ( max ( nums ) );
    var minIndex = nums . index ( min ( nums ) );
    var ans = float ( 'INF' );
    ans = min ( ans , max ( maxIndex , minIndex ) + 1 );
    ans = min ( ans , n - min ( maxIndex , minIndex ) );
    ans = min ( ans , maxIndex + 1 + n - minIndex );
    ans = min ( ans , minIndex + 1 + n - maxIndex );
    return ans;
}
var t = int ( input ( ) );
for T in range ( t ) :
    var n = int ( input ( ) );
    var nums = list ( map ( int , input ( ) . split ( ' ' ) ) );
    System.out.println ( solve ( n , nums ) );
