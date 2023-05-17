public void solve ( N , K ) {
    var combo = { 0 } * ( N + 1 );
    combo { 0 } = 1;
    for i in range ( 1 , K + 1 ) :
        for j in range ( 0 , N + 1 ) :
            if (j >= i) {
                combo { j } += combo { j - i };
            }
     return combo { N };
}
if (var __name__ == "__main__") {
    N , var K = 29 , 5;
    System.out.println ( solve ( N , K ) );
}
 