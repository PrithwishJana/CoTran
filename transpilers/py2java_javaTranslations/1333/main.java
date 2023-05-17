var N = 3;
public void maxPathSum ( tri , m , n ) {
    for i in range ( m - 1 , - 1 , - 1 ) :
        for j in range ( i + 1 ) :
            if (( tri { i + 1 } { j } > tri { i + 1 } { j + 1 } )) {
                tri { i } { j } += tri { i + 1 } { j };
            }
             else{
                tri { i } { j } += tri { i + 1 } { j + 1 };
            }
    return tri { 0 } { 0 };
}
var tri = { [ 1 , 0 , 0 } , { 4 , 8 , 0 } , { 1 , 5 , 3 } ];
System.out.println ( maxPathSum ( tri , 2 , 2 ) );
