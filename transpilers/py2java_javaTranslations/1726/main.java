var limit = 1000000;
var position = { 0 } * ( limit + 1 );
public void sieve ( ) {
    position { 0 } = - 1;
    position { 1 } = - 1;
    var pos = 0;
    for i in range ( 2 , limit + 1 ) :
        if (( position { i } == 0 )) {
            pos += 1;
            position { i } = pos;
            for j in range ( i * 2 , limit + 1 , i ) :
                position { j } = - 1;
        }
 }
if (var __name__ == "__main__") {
    sieve ( );
    var n = 11;
    System.out.println ( position { n } );
}
 