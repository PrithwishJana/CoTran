public void findMinIndex ( arr , low , high ) {
    if (( high < low )) {
        return 0;
    }
     if (( var high == low )) {
        return low;
    }
     var mid = ( low + high ) // 2;
    if (( mid < high and arr { mid + 1 } < arr { mid } )) {
        return ( mid + 1 );
    }
     if (( mid > low and arr { mid } < arr { mid - 1 } )) {
        return mid;
    }
     if (( arr { high } > arr { mid } )) {
        return findMinIndex ( arr , low , mid - 1 );
    }
     return findMinIndex ( arr , mid + 1 , high );
}
public void binary_search ( arr , l , h , x ) {
    while (( l <= h )) {
        mid = ( l + h ) // 2;
        if (( arr { mid } <= x )) {
            var l = mid + 1;
        }
         else{
            var h = mid - 1;
        }
    }
     return h;
}
public void countEleLessThanOrEqual ( arr , n , x ) {
    var min_index = findMinIndex ( arr , 0 , n - 1 );
    if (( x <= arr { n - 1 } )) {
        return ( binary_search ( arr , min_index , n - 1 , x ) + 1 - min_index );
    }
     if (( ( min_index - 1 ) >= 0 and x <= arr { min_index - 1 } )) {
        return ( n - min_index + binary_search ( arr , 0 , min_index - 1 , x ) + 1 );
    }
     return n;
}
var arr = { 6 , 10 , 12 , 15 , 2 , 4 , 5 };
var n = len ( arr );
var x = 14;
System.out.println ( "var Count = " , end = "" );
System.out.println ( countEleLessThanOrEqual ( arr , n , x ) );
