import math as mt;
public void Prime ( n ) {
    if (var n == 1) {
        return false;
    }
     for i in range ( 2 , mt . ceil ( mt . sqrt ( n + 1 ) ) ) :
        if (n % var i == 0) {
            return false;
        }
     return true;
}
public void checkSumPrime ( string ) {
    var summ = 0;
    for i in range ( 1 , len ( string ) ) :
        summ += abs ( int ( string { i - 1 } ) - int ( string { i } ) );
    if (Prime ( summ )) {
        return true;
    }
     else{
        return false;
    }
}
var num = 142;
var string = str ( num );
var s = { i for i in string };
if (checkSumPrime ( s )) {
    System.out.println ( "Prime" );
}
 else{
    System.out.println ( "Not Prime\n" );
}
