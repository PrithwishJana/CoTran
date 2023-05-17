var N = 4;
public void MaximumDecimalValue ( mat , n ) {
    var dp = { [ 0 for i in range ( n ) } for i in range ( n ) ];
    if (( mat { 0 } { 0 } == 1 )) {
        dp { 0 } { 0 } = 1;
    }
     for i in range ( 1 , n ) :
        if (( mat { 0 } { i } == 1 )) {
            dp { 0 } { i } = dp { 0 } { i - 1 } + 2 ** i;
        }
         else{
            dp { 0 } { i } = dp { 0 } { i - 1 };
        }
    for i in range ( 1 , n ) :
        if (( mat { i } { 0 } == 1 )) {
            dp { i } { 0 } = dp { i - 1 } { 0 } + 2 ** i;
        }
     else{
        dp { i } { 0 } = dp { i - 1 } { 0 };
    }
    for i in range ( 1 , n ) :
        for j in range ( 1 , n ) :
            if (( mat { i } { j } == 1 )) {
                dp { i } { j } = max ( dp { i } { j - 1 } , dp { i - 1 } { j } ) + ( 2 ** ( i + j ) );
            }
             else{
                dp { i } { j } = max ( dp { i } { j - 1 } , dp { i - 1 } { j } );
            }
    return dp { n - 1 } { n - 1 };
}
if (var __name__ == '__main__') {
    var mat = { [ 1 , 1 , 0 , 1 } , { 0 , 1 , 1 , 0 } , { 1 , 0 , 0 , 1 } , { 1 , 0 , 1 , 1 } ];
    System.out.println ( MaximumDecimalValue ( mat , 4 ) );
}
 