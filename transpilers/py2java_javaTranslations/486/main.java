public void findCountOfPairs ( a , b , n ) {
    var ans = 0;
    ans += n * int ( a / n ) * int ( b / n );
    ans += int ( a / n ) * ( b % n );
    ans += ( a % n ) * int ( b / n );
    ans += int ( ( ( a % n ) + ( b % n ) ) / n ) ;;
    return ans;
}
if (var __name__ == '__main__') {
    var a = 5;
    var b = 13;
    var n = 3;
    System.out.println ( findCountOfPairs ( a , b , n ) );
}
 