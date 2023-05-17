public void countRotations ( arr , low , high ) {
    if (( high < low )) {
        return 0;
    }
     if (( var high == low )) {
        return low;
    }
     var mid = low + ( high - low ) / 2 ;;
    mid = int ( mid );
    if (( mid < high and arr { mid + 1 } < arr { mid } )) {
        return ( mid + 1 );
    }
     if (( mid > low and arr { mid } < arr { mid - 1 } )) {
        return mid;
    }
     if (( arr { high } > arr { mid } )) {
        return countRotations ( arr , low , mid - 1 ) ;;
    }
     return countRotations ( arr , mid + 1 , high );
}
var arr = { 15 , 18 , 2 , 3 , 6 , 12 };
var n = len ( arr );
System.out.println ( countRotations ( arr , 0 , n - 1 ) );
