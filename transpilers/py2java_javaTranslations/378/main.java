public void evenNumSubstring ( str ) {
    var length = len ( str );
    var count = 0;
    for i in range ( 0 , length , 1 ) :
        var temp = ord ( str { i } ) - ord ( '0' );
        if (( temp % var 2 == 0 )) {
            count += ( i + 1 );
        }
     return count;
}
if (var __name__ == '__main__') {
    var str = { '1' , '2' , '3' , '4' };
    System.out.println ( evenNumSubstring ( str ) );
}
 