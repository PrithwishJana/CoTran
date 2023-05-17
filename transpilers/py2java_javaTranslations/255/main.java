public void no_of_ways ( s ) {
    var n = len ( s );
    var count_left = 0;
    var count_right = 0;
    for i in range ( 0 , n , 1 ) :
        if (( s { i } == s { 0 } )) {
            count_left += 1;
        }
         else{
            break;
        }
    var i = n - 1;
    while (( i >= 0 )) {
        if (( s { i } == s { n - 1 } )) {
            count_right += 1;
        }
         else{
            break;
        }
        i -= 1;
    }
     if (( s { 0 } == s { n - 1 } )) {
        return ( ( count_left + 1 ) * ( count_right + 1 ) );
     }
     else{
        return ( count_left + count_right + 1 );
    }
}
if (var __name__ == '__main__') {
    var s = "geeksforgeeks";
    System.out.println ( no_of_ways ( s ) );
}
 