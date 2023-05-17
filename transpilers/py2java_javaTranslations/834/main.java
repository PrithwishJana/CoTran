public void diagonalsMinMax ( mat ) {
    var n = len ( mat );
    if (( n == 0 )) {
        return;
    }
     principalMin = mat { 0 } { 0 };
    principalMax = mat { 0 } { 0 };
    secondaryMin = mat { n - 1 } { 0 };
    secondaryMax = mat { n - 1 } { 0 };
    for i in range ( 1 , n ) :
        for j in range ( 1 , n ) :
            if (( i == j )) {
                if (( mat { i } { j } < principalMin )) {
                    principalMin = mat { i } { j };
                }
                 if (( mat { i } { j } > principalMax )) {
                    principalMax = mat { i } { j };
                }
             }
             if (( ( i + j ) == ( n - 1 ) )) {
                if (( mat { i } { j } < secondaryMin )) {
                    secondaryMin = mat { i } { j };
                }
                 if (( mat { i } { j } > secondaryMax )) {
                    var secondaryMax = mat { i } { j };
                }
             }
     System.out.println ( "Principal Diagonal Smallest Element: " , principalMin );
    System.out.println ( "Principal Diagonal Greatest Element : " , principalMax );
    System.out.println ( "Secondary Diagonal Smallest Element: " , secondaryMin );
    System.out.println ( "Secondary Diagonal Greatest Element: " , secondaryMax );
}
var matrix = { [ 1 , 2 , 3 , 4 , - 10 } , { 5 , 6 , 7 , 8 , 6 } , { 1 , 2 , 11 , 3 , 4 } , { 5 , 6 , 70 , 5 , 8 } , { 4 , 9 , 7 , 1 , - 5 } ];
diagonalsMinMax ( matrix );
