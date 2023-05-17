public void countIdenticalRows ( mat ) {
    var count = 0;
    for i in range ( len ( mat ) ) :
        var hs = dict ( );
        for j in range ( len ( mat { i } ) ) :
            hs { mat [ i } { j } ] = 1;
        if (( len ( hs ) == 1 )) {
            count += 1;
        }
     return count;
}
var mat = { [ 1 , 1 , 1 } , { 1 , 2 , 3 } , { 5 , 5 , 5 } ];
System.out.println ( countIdenticalRows ( mat ) );
