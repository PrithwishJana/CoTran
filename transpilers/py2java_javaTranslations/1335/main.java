public void isHeap ( arr , i , n ) {
    if (i > int ( ( n - 2 ) / 2 )) {
        return true;
    }
     if (( arr { i } >= arr { 2 * i + 1 } and arr { i } >= arr { 2 * i + 2 } and isHeap ( arr , 2 * i + 1 , n ) and isHeap ( arr , 2 * i + 2 , n ) )) {
        return true;
    }
     return false;
}
if (var __name__ == '__main__') {
    var arr = { 90 , 15 , 10 , 7 , 12 , 2 , 7 , 3 };
    var n = len ( arr ) - 1;
    if (isHeap ( arr , 0 , n )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 