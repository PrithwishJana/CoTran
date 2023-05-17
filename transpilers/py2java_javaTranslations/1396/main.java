var MAX = 100;
public void countMountains ( a , n ) {
    var A = { [ 0 for i in range ( n + 2 ) } for i in range ( n + 2 ) ];
    var count = 0;
    for i in range ( n + 2 ) :
        for j in range ( n + 2 ) :
            if (( ( i == 0 ) or ( j == 0 ) or ( i == n + 1 ) or ( j == n + 1 ) )) {
                A { i } { j } = float ( '-inf' );
            }
             else{
                A { i } { j } = a { i - 1 } { j - 1 };
            }
    for i in range ( n + 1 ) :
        for j in range ( n + 1 ) :
            if (( ( A { i } { j } > A { i - 1 } { j } ) and ( A { i } { j } > A { i + 1 } { j } ) and ( A { i } { j } > A { i } { j - 1 } ) and ( A { i } { j } > A { i } { j + 1 } ) and ( A { i } { j } > A { i - 1 } { j - 1 } ) and ( A { i } { j } > A { i + 1 } { j + 1 } ) and ( A { i } { j } > A { i - 1 } { j + 1 } ) and ( A { i } { j } > A { i + 1 } { j - 1 } ) )) {
                count = count + 1;
            }
     return count;
}
var a = { [ 1 , 2 , 3 } , { 4 , 5 , 6 } , { 7 , 8 , 9 } ];
var n = 3;
System.out.println ( countMountains ( a , n ) );
