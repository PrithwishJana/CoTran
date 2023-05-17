public void firstkdigits ( n , k ) {
    var product = 1;
    for i in range ( n ) :
        product *= n;
    while (( ( product // pow ( 10 , k ) ) != 0 )) {
        product = product // 10;
    }
     return product;
}
var n = 15;
var k = 4;
System.out.println ( firstkdigits ( n , k ) );
