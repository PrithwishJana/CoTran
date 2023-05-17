var DP_s = 9;
public void getNumMonotone ( ln ) {
    var DP = { [ 0 } * DP_s for i in range ( ln ) ];
    for i in range ( DP_s ) :
        DP { 0 } { i } = i + 1;
    for i in range ( ln ) :
        DP { i } { 0 } = 1;
    for i in range ( 1 , ln ) :
        for j in range ( 1 , DP_s ) :
            DP { i } { j } = DP { i - 1 } { j } + DP { i } { j - 1 };
    return DP { ln - 1 } { DP_s - 1 };
}
System.out.println ( getNumMonotone ( 10 ) );
