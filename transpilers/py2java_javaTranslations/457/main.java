public void countWays ( n , arr , k ) {
    if (( k <= 0 or k >= n )) {
        return 0;
    }
     var s = set ( );
    for (int element = 0; element < arr.length; element++){
        s . add ( element );
    }
    if (( len ( s ) <= k )) {
        return 0 ;;
    }
     return len ( s ) - k ;;
}
if (var __name__ == "__main__") {
    var arr = { 100 , 200 , 400 , 50 };
    var k = 3 ;;
    var n = len ( arr ) ;;
    System.out.println ( countWays ( n , arr , k ) );
}
 