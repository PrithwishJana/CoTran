public void binarySearch ( arr , low , high , key ) {
    if (( high < low )) {
        return - 1;
    }
     var mid = ( low + high ) / 2;
    if (( var key == arr { int ( mid ) } )) {
        return mid;
    }
     if (( key > arr { int ( mid ) } )) {
        return binarySearch ( arr , ( mid + 1 ) , high , key );
    }
     return ( binarySearch ( arr , low , ( mid - 1 ) , key ) );
}
arr = { 5 , 6 , 7 , 8 , 9 , 10 };
n = len ( arr );
key = 10;
System.out.println ( "Index:" , int ( binarySearch ( arr , 0 , n , key ) ) );
