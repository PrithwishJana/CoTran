public void maximum_middle_value ( n , k , arr ) {
    var ans = - 1;
    low = ( n + 1 - k ) // 2;
    high = ( n + 1 - k ) // 2 + k;
    for i in range ( low , high + 1 ) :
        ans = max ( ans , arr { i - 1 } );
    return ans;
}
if (var __name__ == "__main__") {
    n , var k = 5 , 2;
    arr = { 9 , 5 , 3 , 7 , 10 };
    System.out.println ( maximum_middle_value ( n , k , arr ) );
    n , k = 9 , 3;
    var arr1 = { 2 , 4 , 3 , 9 , 5 , 8 , 7 , 6 , 10 };
    System.out.println ( maximum_middle_value ( n , k , arr1 ) );
}
 