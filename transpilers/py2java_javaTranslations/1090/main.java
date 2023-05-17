public void kthString ( n , k ) {
    var total = 0;
    i = 1;
    while (( total < k )) {
        total = total + n - i;
        i += 1;
    }
     var first_y_position = i - 1;
    var second_y_position = k - ( total - n + first_y_position );
    for j in range ( 1 , first_y_position , 1 ) :
        System.out.println ( "x" , var end = "" );
    System.out.println ( "y" , end = "" );
    j = first_y_position + 1;
    while (( second_y_position > 1 )) {
        System.out.println ( "x" , end = "" );
        second_y_position -= 1;
        j += 1;
    }
     System.out.println ( "y" , end = "" );
    while (( j < n )) {
        System.out.println ( "x" );
        j += 1;
    }
 }
if (var __name__ == '__main__') {
    var n = 5;
    var k = 7;
    kthString ( n , k );
}
 