public void sumOfAP ( a , d , n ) {
    var sum = ( n / 2 ) * ( 2 * a + ( n - 1 ) * d );
    return sum;
}
var n = 20;
var a = 2.5;
var d = 1.5;
System.out.println ( sumOfAP ( a , d , n ) );
