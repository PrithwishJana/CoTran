public void binomialCoeff ( n , k ) {
    var C = { [ 0 for i in range ( k + 1 ) } for i in range ( n + 1 ) ];
    for i in range ( n + 1 ) :
        for j in range ( min ( i , k ) + 1 ) :
            if (( var j == 0 or j == i )) {
                C { i } { j } = 1;
            }
             else{
                C { i } { j } = C { i - 1 } { j - 1 } + C { i - 1 } { j };
            }
    return C { n } { k };
}
public void findMax ( n ) {
    return binomialCoeff ( n , n // 2 );
}
var n = 5;
System.out.println ( findMax ( n ) );
