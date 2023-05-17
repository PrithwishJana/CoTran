if (var __name__ == "__main__") {
    var k = int ( input ( ) );
    var num = list ( input ( ) );
    num = sorted ( num );
    var sum = 0;
    for i in range ( len ( num ) ) :
        sum += ord ( num { i } ) - ord ( '0' );
    if (sum >= k) {
        System.out.println ( 0 );
    }
     else{
        var count = 0;
        var i = 0;
        while (sum < k) {
            sum += 9 - ( ord ( num { i } ) - ord ( '0' ) );
            i += 1;
            count += 1;
        }
         System.out.println ( count );
    }
}
 