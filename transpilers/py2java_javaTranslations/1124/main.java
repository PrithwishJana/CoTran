public void compute ( ) {
    var SIZE_LIMIT = 1000000;
    var TYPE_LIMIT = 10;
    var type = { 0 } * ( SIZE_LIMIT + 1 );
    for n in range ( 3 , SIZE_LIMIT // 4 + 2 ) :
        for m in range ( n - 2 , 0 , - 2 ) :
            var tiles = n * n - m * m;
            if (tiles > SIZE_LIMIT) {
                break;
            }
             type { tiles } += 1;
    var ans = sum ( 1 for t in type if 1 <= t <= TYPE_LIMIT );
    return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 