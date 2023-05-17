public void countNonDecreasing ( n ) {
    var N = 10;
    var count = 1;
    for i in range ( 1 , n + 1 ) :
        count = int ( count * ( N + i - 1 ) );
        count = int ( count / i );
    return count;
}
var n = 3 ;;
System.out.println ( countNonDecreasing ( n ) );
