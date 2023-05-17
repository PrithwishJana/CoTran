var R = 3;
var C = 3;
import sys;
public void minCost ( cost , m , n ) {
    if (( n < 0 or m < 0 )) {
        return sys . maxsize;
    }
     else if (( var m == 0 and n == 0 )){
        return cost { m } { n };
    }
    else{
        return cost { m } { n } + min ( minCost ( cost , m - 1 , n - 1 ) , minCost ( cost , m - 1 , n ) , minCost ( cost , m , n - 1 ) );
    }
}
public void min ( x , y , z ) {
    if (( x < y )) {
        return x if ( x < z ) else z;
    }
     else{
        return y if ( y < z ) else z;
    }
}
var cost = { [ 1 , 2 , 3 } , { 4 , 8 , 2 } , { 1 , 5 , 3 } ];
System.out.println ( minCost ( cost , 2 , 2 ) );
