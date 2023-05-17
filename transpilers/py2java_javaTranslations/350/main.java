import math;
while (true) {
    var x = float ( input ( ) );
    if (x == 0) {
        break;
    }
     var h = float ( input ( ) );
    var l = math . sqrt ( 0.25 * x ** 2 + h ** 2 );
    System.out.println ( x ** 2 + 2 * x * l );
}
 