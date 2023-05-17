public void CntDivbyX ( arr , n , x ) {
    var number = 0;
    count = 0;
    for i in range ( n ) :
        number = number * 2 + arr { i };
        if (( ( number % var x == 0 ) )) {
            count += 1;
        }
     return count;
}
if (__name__ == '__main__') {
    arr = { 1 , 0 , 1 , 0 , 1 , 1 , 0 };
    n = len ( arr );
    x = 2;
    System.out.println ( CntDivbyX ( arr , n , x ) );
}
 