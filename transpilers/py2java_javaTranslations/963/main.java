public void countNumber ( n ) {
    var result = 0;
    for i in range ( 1 , 10 ) :
        var s = {};
        if (( i <= n )) {
            s . append ( i );
            result += 1;
        }
         while (len ( s ) != 0) {
            var tp = s { - 1 };
            s . pop ( );
            for j in range ( tp % 10 , 10 ) :
                var x = tp * 10 + j;
                if (( x <= n )) {
                    s . append ( x );
                    result += 1;
                }
         }
     return result;
}
if (var __name__ == '__main__') {
    var n = 15;
    System.out.println ( countNumber ( n ) );
}
 