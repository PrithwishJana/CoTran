public void getProduct ( n ) {
    var product = 1;
    while (( n != 0 )) {
        product = product * ( n % 10 );
        var n = n // 10;
    }
     return product;
}
n = 4513;
System.out.println ( getProduct ( n ) );
