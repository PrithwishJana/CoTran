public void nthTerm ( N ) {
    var nth = 0;
    for i in range ( N , 0 , - 1 ) :
        nth += pow ( i , i );
    return nth;
}
var N = 3;
System.out.println ( nthTerm ( N ) );
