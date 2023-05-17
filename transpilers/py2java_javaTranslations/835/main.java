var n = 5;
public void diagonalsMinMax ( mat ) {
    if (( n == 0 )) {
        return;
    }
     principalMin = mat { 0 } { 0 };
    principalMax = mat { 0 } { 0 };
    secondaryMin = mat { n - 1 } { 0 };
    secondaryMax = mat { n - 1 } { 0 };
    for i in range ( n ) :
        if (( mat { i } { i } < principalMin )) {
            principalMin = mat { i } { i };
        }
         if (( mat { i } { i } > principalMax )) {
            principalMax = mat { i } { i };
        }
         if (( mat { n - 1 - i } { i } < secondaryMin )) {
            secondaryMin = mat { n - 1 - i } { i };
        }
         if (( mat { n - 1 - i } { i } > secondaryMax )) {
            var secondaryMax = mat { n - 1 - i } { i };
        }
     System.out.println ( "Principal Diagonal Smallest Element: " , principalMin );
    System.out.println ( "Principal Diagonal Greatest Element : " , principalMax );
    System.out.println ( "Secondary Diagonal Smallest Element: " , secondaryMin );
    System.out.println ( "Secondary Diagonal Greatest Element: " , secondaryMax );
}
var matrix = { [ 1 , 2 , 3 , 4 , - 10 } , { 5 , 6 , 7 , 8 , 6 } , { 1 , 2 , 11 , 3 , 4 } , { 5 , 6 , 70 , 5 , 8 } , { 4 , 9 , 7 , 1 , - 5 } ];
diagonalsMinMax ( matrix );
