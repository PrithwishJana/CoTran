public void removeZero ( n ) {
    var res = 0;
    var d = 1;
    while (( n > 0 )) {
        if (( n % 10 != 0 )) {
            res += ( n % 10 ) * d;
            d *= 10;
        }
         n //= 10;
    }
     return res;
}
public void isEqual ( a , b ) {
    if (( removeZero ( a ) + removeZero ( b ) == removeZero ( a + b ) )) {
        return true;
    }
     return false;
}
var a = 105;
var b = 106;
if (( isEqual ( a , b ) )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
