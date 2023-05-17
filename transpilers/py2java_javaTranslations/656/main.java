import math.sqrt;
public void checkDivisors ( a , n ) {
    var X = max ( a );
    var b = {};
    for i in range ( 1 , int ( sqrt ( X ) ) + 1 ) :
        if (( X % var i == 0 )) {
            b . append ( i );
            if (( X // i != i )) {
                b . append ( X // i );
            }
         }
     if (( len ( b ) != n )) {
        return false;
    }
     a . sort ( var reverse = false );
    b . sort ( reverse = false );
    for i in range ( n ) :
        if (( b { i } != a { i } )) {
            return false;
        }
     return true;
}
if (var __name__ == '__main__') {
    var arr = { 8 , 1 , 2 , 12 , 48 , 6 , 4 , 24 , 16 , 3 };
    var N = len ( arr );
    if (( checkDivisors ( arr , N ) )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 