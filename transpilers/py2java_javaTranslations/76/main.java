public void fact ( N ) {
    var product = 1;
    for i in range ( 1 , N + 1 ) :
        product = product * i;
    return product;
}
public void nthTerm ( N ) {
    return ( N * N ) * fact ( N );
}
if (var __name__ == "__main__") {
    var N = 4;
    System.out.println ( nthTerm ( N ) );
}
 