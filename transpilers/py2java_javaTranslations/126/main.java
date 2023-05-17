public void lcsOf3 ( X , Y , Z , m , n , o ) {
    var L = { [ [ 0 for i in range ( o + 1 ) } for j in range ( n + 1 ) ] for k in range ( m + 1 ) ];
    for i in range ( m + 1 ) :
        for j in range ( n + 1 ) :
            for k in range ( o + 1 ) :
                if (( var i == 0 or j == 0 or k == 0 )) {
                    L { i } { j } { k } = 0;
                }
                 else if (( X { i - 1 } == Y { j - 1 } and X { i - 1 } == Z { k - 1 } )){
                    L { i } { j } { k } = L { i - 1 } { j - 1 } { k - 1 } + 1;
                }
                else{
                    L { i } { j } { k } = max ( max ( L { i - 1 } { j } { k } , L { i } { j - 1 } { k } ) , L { i } { j } { k - 1 } );
                }
    return L { m } { n } { o };
}
var X = 'AGGT12';
var Y = '12TXAYB';
var Z = '12XBA';
var m = len ( X );
var n = len ( Y );
var o = len ( Z );
System.out.println ( 'Length of LCS is' , lcsOf3 ( X , Y , Z , m , n , o ) );
