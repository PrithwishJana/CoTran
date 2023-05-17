import math;
public void countDigits ( a , b ) {
    if (( var a == 0 or b == 0 )) {
        return 1;
    }
     return math . floor ( math . log10 ( abs ( a ) ) + math . log10 ( abs ( b ) ) ) + 1;
}
a = 33;
var b = - 24;
System.out.println ( countDigits ( a , b ) );
