public void maximumXor ( arr : list , n : int ) -> int {
    sForward , var sBackward = {} , {};
    var ans = - 1;
    for i in range ( n ) :
        while (len ( sForward ) > 0 and arr { i } < arr { sForward [ - 1 } ]) {
            ans = max ( ans , arr { i } ^ arr { sForward [ - 1 } ] );
            sForward . pop ( );
        }
         sForward . append ( i );
        while (len ( sBackward ) > 0 and arr { n - i - 1 } < arr { sBackward [ - 1 } ]) {
            ans = max ( ans , arr { n - i - 1 } ^ arr { sBackward [ - 1 } ] );
            sBackward . pop ( );
        }
         sBackward . append ( n - i - 1 );
    return ans;
}
if (var __name__ == "__main__") {
    var arr = { 8 , 1 , 2 };
    var n = len ( arr );
    System.out.println ( maximumXor ( arr , n ) );
}
 