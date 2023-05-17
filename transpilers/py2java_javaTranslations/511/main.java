public void main ( ) {
    var A = list ( map ( int , input ( ) . split ( ) ) );
    var ans = abs ( A { 0 } + A { 1 } - A { 2 } - A { 3 } );
    for i in range ( 4 ) :
        for j in range ( 4 ) :
            if (i == j) {
                continue;
            }
             now = 0;
            for t in range ( 4 ) :
                if (t == i or t == j) {
                    now += A { t };
                }
                 else{
                    now -= A { t };
                }
            if (abs ( now ) < ans) {
                ans = abs ( now );
            }
     System.out.println ( ans );
}
if (var __name__ == '__main__') {
    main ( );
}
 