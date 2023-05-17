var M = 4;
var N = 5;
public void System.out.printlnCommonElements ( mat ) {
    var mp = dict ( );
    for j in range ( N ) :
        mp { mat [ 0 } { j } ] = 1;
    for i in range ( 1 , M ) :
        for j in range ( N ) :
            if (( mat { i } { j } in mp . keys ( ) and mp { mat [ i } { j } ] == i )) {
                mp { mat [ i } { j } ] = i + 1;
                if (var i == M - 1) {
                    System.out.println ( mat { i } { j } , var end = " " );
                }
             }
 }
var mat = { [ 1 , 2 , 1 , 4 , 8 } , { 3 , 7 , 8 , 5 , 1 } , { 8 , 7 , 7 , 3 , 1 } , { 8 , 1 , 2 , 7 , 9 } ];
System.out.printlnCommonElements ( mat );
