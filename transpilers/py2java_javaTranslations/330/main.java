public void System.out.printlnSumTricky ( mat , k ) {
    global n;
    if (k > n) {
        return;
    }
     var stripSum = { [ None } * n for i in range ( n ) ];
    for j in range ( n ) :
        var Sum = 0;
        for i in range ( k ) :
            Sum += mat { i } { j };
        stripSum { 0 } { j } = Sum;
        for i in range ( 1 , n - k + 1 ) :
            Sum += ( mat { i + k - 1 } { j } - mat { i - 1 } { j } );
            stripSum { i } { j } = Sum;
    for i in range ( n - k + 1 ) :
        Sum = 0;
        for j in range ( k ) :
            Sum += stripSum { i } { j };
        System.out.println ( Sum , var end = " " );
        for j in range ( 1 , n - k + 1 ) :
            Sum += ( stripSum { i } { j + k - 1 } - stripSum { i } { j - 1 } );
            System.out.println ( Sum , end = " " );
        System.out.println ( );
}
var n = 5;
var mat = { [ 1 , 1 , 1 , 1 , 1 } , { 2 , 2 , 2 , 2 , 2 } , { 3 , 3 , 3 , 3 , 3 } , { 4 , 4 , 4 , 4 , 4 } , { 5 , 5 , 5 , 5 , 5 } ];
var k = 3;
System.out.printlnSumTricky ( mat , k );
