import math;
public void findIndex ( n ) {
    var fibo = 2.078087 * math . log ( n ) + 1.672276;
    return round ( fibo );
}
var n = 21;
System.out.println ( findIndex ( n ) );
