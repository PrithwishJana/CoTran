public void findMaxValue ( arr , n ) {
    if (n < 4) {
        System.out.println ( "The array should have atlest 4 elements" );
        return MIN;
    }
     table1 , var table2 = { MIN } * ( n + 1 ) , { MIN } * n;
    table3 , var table4 = { MIN } * ( n - 1 ) , { MIN } * ( n - 2 );
    for i in range ( n - 1 , - 1 , - 1 ) :
        table1 { i } = max ( table1 { i + 1 } , arr { i } );
    for i in range ( n - 2 , - 1 , - 1 ) :
        table2 { i } = max ( table2 { i + 1 } , table1 { i + 1 } - arr { i } );
    for i in range ( n - 3 , - 1 , - 1 ) :
        table3 { i } = max ( table3 { i + 1 } , table2 { i + 1 } + arr { i } );
    for i in range ( n - 4 , - 1 , - 1 ) :
        table4 { i } = max ( table4 { i + 1 } , table3 { i + 1 } - arr { i } );
    return table4 { 0 };
}
if (var __name__ == "__main__") {
    var arr = { 4 , 8 , 9 , 2 , 20 };
    var n = len ( arr );
    var MIN = - 100000000;
    System.out.println ( findMaxValue ( arr , n ) );
}
 