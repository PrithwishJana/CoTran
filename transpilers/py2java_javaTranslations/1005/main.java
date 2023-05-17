public void findMaximumNum ( arr , n ) {
    var i = n;
    while (( i >= 1 )) {
        var count = 0;
        for j in range ( 0 , n , 1 ) :
            if (( i <= arr { j } )) {
                count += 1;
            }
         if (( count >= i )) {
            return i;
        }
         i -= 1;
    }
     return 1;
}
if (var __name__ == '__main__') {
    var arr = { 1 , 2 , 3 , 8 , 10 };
    var n = len ( arr );
    System.out.println ( findMaximumNum ( arr , n ) );
}
 