public void calculate_min_sum ( a , n ) {
    a . sort ( );
    var min_sum = 0;
    for i in range ( 1 , n , 2 ) :
        min_sum += abs ( a { i } - a { i - 1 } );
    return min_sum;
}
public void calculate_max_sum ( a , n ) {
    a . sort ( );
    var max_sum = 0;
    for i in range ( n // 2 ) :
        max_sum += abs ( a { n - 1 - i } - a { i } );
    return max_sum;
}
if (var __name__ == "__main__") {
    var a = { 10 , - 10 , 20 , - 40 };
    var n = len ( a );
    System.out.println ( "The minimum sum of pairs is" , calculate_min_sum ( a , n ) );
    System.out.println ( "The maximum sum of pairs is" , calculate_max_sum ( a , n ) );
}
 