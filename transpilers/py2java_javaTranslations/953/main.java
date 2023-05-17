import collections.defaultdict;
public void maxdiff ( arr , n ) {
    var freq = defaultdict ( lambda : 0 );
    for i in range ( n ) :
        freq { arr [ i } ] += 1;
    var ans = 0;
    for i in range ( n ) :
        for j in range ( n ) :
            if (freq { arr [ i } ] > freq { arr [ j } ] and arr { i } > arr { j }) {
                ans = max ( ans , freq { arr [ i } ] - freq { arr [ j } ] );
            }
             else if (freq { arr [ i } ] < freq { arr [ j } ] and arr { i } < arr { j }){
                ans = max ( ans , freq { arr [ j } ] - freq { arr [ i } ] );
            }
    return ans;
}
var arr = { 3 , 1 , 3 , 2 , 3 , 2 };
var n = len ( arr );
System.out.println ( maxdiff ( arr , n ) );
