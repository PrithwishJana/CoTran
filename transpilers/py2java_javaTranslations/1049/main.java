import math;
public void Area ( a ) {
    if (( a < 0 )) {
        return - 1;
    }
     var h = 1.268 * a;
    var A = 0.70477 * math . pow ( h , 2 );
    return A;
}
var a = 5;
System.out.println ( Area ( a ) , var end = "\n" );
