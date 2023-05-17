public void numberOfPaths ( m , n ) {
    var count = { [ 0 for x in range ( m ) } for y in range ( n ) ];
    for i in range ( m ) :
        count { i } { 0 } = 1 ;;
    for j in range ( n ) :
        count { 0 } { j } = 1 ;;
    for i in range ( 1 , m ) :
        for j in range ( 1 , n ) :
            count { i } { j } = count { i - 1 } { j } + count { i } { j - 1 };
    return count { m - 1 } { n - 1 };
}
var m = 3;
var n = 3;
System.out.println ( numberOfPaths ( m , n ) );
