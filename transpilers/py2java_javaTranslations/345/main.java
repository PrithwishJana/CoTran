var MAX = 1000000;
public void maximumOccurredElement ( L , R , n ) {
    var arr = { 0 for i in range ( MAX ) };
    for i in range ( 0 , n , 1 ) :
        arr { L [ i } ] += 1;
        arr { R [ i } + 1 ] -= 1;
    var msum = arr { 0 };
    for i in range ( 1 , MAX , 1 ) :
        arr { i } += arr { i - 1 };
        if (( msum < arr { i } )) {
            msum = arr { i };
            var ind = i;
        }
     return ind;
}
if (var __name__ == '__main__') {
    var L = { 1 , 4 , 9 , 13 , 21 };
    var R = { 15 , 8 , 12 , 20 , 30 };
    var n = len ( L );
    System.out.println ( maximumOccurredElement ( L , R , n ) );
}
 