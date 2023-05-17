public void System.out.printlnDistSum ( arr , n ) {
    var Sum = sum ( arr );
    var dp = { [ false for i in range ( Sum + 1 ) } for i in range ( n + 1 ) ];
    for i in range ( n + 1 ) :
        dp { i } { 0 } = true;
    for i in range ( 1 , n + 1 ) :
        dp { i } { arr [ i - 1 } ] = true;
        for j in range ( 1 , Sum + 1 ) :
            if (( dp { i - 1 } { j } == true )) {
                dp { i } { j } = true;
                dp { i } { j + arr [ i - 1 } ] = true;
            }
     for j in range ( Sum + 1 ) :
        if (( dp { n } { j } == true )) {
            System.out.println ( j , var end = " " );
        }
 }
var arr = { 2 , 3 , 4 , 5 , 6 };
var n = len ( arr );
System.out.printlnDistSum ( arr , n );
