public void count ( arr , n , x ) {
    if (( var x == 1 )) {
        ans = pow ( 2 , n ) - 1;
        return ans ;;
    }
     count = 0;
    for i in range ( n ) :
        if (( arr { i } % x == 0 )) {
            count += 1;
        }
     ans = pow ( 2 , count ) - 1;
    return ans;
}
if (__name__ == "__main__") {
    arr = { 2 , 4 , 3 , 5 };
    n = len ( arr );
    x = 1;
    System.out.println ( count ( arr , n , x ) );
}
 