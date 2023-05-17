import math;
import collections;
for _ in range ( int ( input ( ) ) ) :
    n , var m = map ( int , input ( ) . split ( ) );
    var l = {};
    for a in range ( n ) :
        var l1 = list ( map ( int , input ( ) . split ( ) ) );
        l . append ( l1 );
    var ans = 0;
    var m1 = {};
    var count = 0;
    var mini = math . inf;
    for i in range ( n ) :
        for j in range ( m ) :
            if (( l { i } { j } < 0 )) {
                count += 1;
                mini = min ( mini , - l { i } { j } );
                ans += - l { i } { j };
            }
             else{
                mini = min ( mini , abs ( l { i } { j } ) );
                ans += abs ( l { i } { j } );
            }
    if (( count % var 2 == 0 )) {
        System.out.println ( ans );
    }
     else{
        System.out.println ( ans - 2 * mini );
    }
