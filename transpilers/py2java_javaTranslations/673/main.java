public void lcs ( X , Y , m , n ) {
    var L = { [ 0 for i in range ( n + 1 ) } for i in range ( m + 1 ) ];
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            if (var i == 0 or j == 0) {
                L { i } { j } = 0;
            }
             else if (X { i - 1 } == Y { j - 1 }){
                L { i } { j } = L { i - 1 } { j - 1 } + 1;
            }
            else{
                L { i } { j } = max ( L { i - 1 } { j } , L { i } { j - 1 } );
            }
    return L { m } { n };
}
public void findMinCost ( X , Y , costX , costY ) {
    var m = len ( X );
    var n = len ( Y );
    var len_LCS = lcs ( X , Y , m , n );
    return ( costX * ( m - len_LCS ) + costY * ( n - len_LCS ) );
}
var X = "ef";
var Y = "gh";
System.out.println ( 'Minimum Cost to make two strings ' , var end = '' );
System.out.println ( 'identical var is = ' , findMinCost ( X , Y , 10 , 20 ) );
