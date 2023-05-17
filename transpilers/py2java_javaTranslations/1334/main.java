public void isHeap ( arr , n ) {
    for i in range ( int ( ( n - 2 ) / 2 ) + 1 ) :
        if (arr { 2 * i + 1 } > arr { i }) {
            return false;
        }
         if (( 2 * i + 2 < n and arr { 2 * i + 2 } > arr { i } )) {
            return false;
        }
     return true;
}
if (var __name__ == '__main__') {
    var arr = { 90 , 15 , 10 , 7 , 12 , 2 , 7 , 3 };
    var n = len ( arr );
    if (isHeap ( arr , n )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 