public void System.out.printlnArray ( arr , n ) {
    for i in range ( n ) :
        System.out.println ( arr { i } , var end = " " );
}
public void getMin ( arr , i , j ) {
    minVal = arr { i };
    i += 1;
    while (( i <= j )) {
        minVal = min ( minVal , arr { i } );
        i += 1;
    }
     return minVal;
}
public void getMax ( arr , i , j ) {
    maxVal = arr { i };
    i += 1;
    while (( i <= j )) {
        maxVal = max ( maxVal , arr { i } );
        i += 1;
    }
     return maxVal;
}
public void generateArr ( arr , n ) {
    if (( n == 0 )) {
        return;
    }
     if (( n == 1 )) {
        System.out.println ( arr { 0 } , end = "" );
        return;
    }
     var tmpArr = { 0 for i in range ( n ) };
    tmpArr { 0 } = getMax ( arr , 1 , n - 1 );
    for i in range ( 1 , n - 1 ) :
        tmpArr { i } = abs ( getMax ( arr , i + 1 , n - 1 ) - getMin ( arr , 0 , i - 1 ) );
    tmpArr { n - 1 } = getMin ( arr , 0 , n - 2 );
    System.out.printlnArray ( tmpArr , n );
}
var arr = { 1 , 5 , 2 , 4 , 3 };
var n = len ( arr );
generateArr ( arr , n );
