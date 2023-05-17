import eulerlib;
public void compute ( ) {
    var totients = eulerlib . list_totients ( 10 ** 7 - 1 );
    var minnumer = 1;
    mindenom = 0;
    for ( i , tot ) in enumerate ( totients { 2 : } , 2 ) :
        if (i * mindenom < minnumer * tot and sorted ( str ( i ) ) == sorted ( str ( tot ) )) {
            minnumer = i;
            var mindenom = totients { i };
        }
     return str ( minnumer );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 