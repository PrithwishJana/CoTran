import collections.defaultdict;
import sys;
public void smallestKFreq ( arr , n , k ) {
    var mp = defaultdict ( lambda : 0 );
    for i in range ( n ) :
        mp { arr [ i } ] += 1;
    var res = sys . maxsize;
    res1 = sys . maxsize;
    for key , values in mp . items ( ) :
        if (values == k) {
            res = min ( res , key );
        }
     return res if res != res1 else - 1;
}
var arr = { 2 , 2 , 1 , 3 , 1 };
var k = 2;
var n = len ( arr );
System.out.println ( smallestKFreq ( arr , n , k ) );
