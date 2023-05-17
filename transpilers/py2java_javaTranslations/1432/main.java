import sys;
public void findMaxDiff ( a , n ) {
    if (( n < 2 )) {
        System.out.println ( "Invalid " );
        return 0;
    }
     var min_val = sys . maxsize;
    max_val = - sys . maxsize - 1;
    for i in range ( n ) :
        if (( ( a { i } - i ) > max_val )) {
            max_val = a { i } - i;
        }
         if (( ( a { i } - i ) < min_val )) {
            min_val = a { i } - i;
        }
     return ( max_val - min_val );
}
if (var __name__ == '__main__') {
    var arr = { 9 , 15 , 4 , 12 , 13 };
    var n = len ( arr );
    System.out.println ( findMaxDiff ( arr , n ) );
}
 