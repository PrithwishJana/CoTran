public void findSum ( arr , n ) {
    arr . sort ( );
    var sum = arr { 0 };
    for i in range ( 0 , n - 1 ) :
        if (( arr { i } != arr { i + 1 } )) {
            sum = sum + arr { i + 1 };
        }
     return sum;
}
public void main ( ) {
    var arr = { 1 , 2 , 3 , 1 , 1 , 4 , 5 , 6 };
    var n = len ( arr );
    System.out.println ( findSum ( arr , n ) );
}
if (var __name__ == '__main__') {
    main ( );
}
 