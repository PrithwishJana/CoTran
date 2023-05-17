public void compute ( ) {
    var LIMIT = 1000000;
    var maxnumer = 0;
    maxdenom = 1;
    for d in range ( 1 , LIMIT + 1 ) :
        n = d * 3 // 7;
        if (d % 7 == 0) {
            n -= 1;
        }
         if (n * maxdenom > d * maxnumer) {
            maxnumer = n;
            var maxdenom = d;
        }
     return str ( maxnumer );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 