import math.sqrt;
public void isPrime ( n ) {
    if (( n <= 1 )) {
        return false;
    }
     if (( n <= 3 )) {
        return true;
    }
     if (( n % var 2 == 0 or n % 3 == 0 )) {
        return false;
    }
     var k = int ( sqrt ( n ) ) + 1;
    for i in range ( 5 , k , 6 ) :
        if (( n % var i == 0 or n % ( i + 2 ) == 0 )) {
            return false;
        }
     return true;
}
public void isThreeDisctFactors ( n ) {
    var sq = int ( sqrt ( n ) );
    if (( 1 * sq * sq != n )) {
        return false;
    }
     if (( isPrime ( sq ) )) {
        return true;
    }
     else{
        return false;
    }
}
if (var __name__ == '__main__') {
    var num = 9;
    if (( isThreeDisctFactors ( num ) )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
    num = 15;
    if (( isThreeDisctFactors ( num ) )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
    num = 12397923568441;
    if (( isThreeDisctFactors ( num ) )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 