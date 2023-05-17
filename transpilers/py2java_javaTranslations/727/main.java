import math;
public void check ( a , y ) {
    var sum = 0;
    for i in range ( len ( a ) ) :
        x = math . sqrt ( a { i } );
        if (( math . floor ( x ) == math . ceil ( x ) )) {
            sum = sum + a { i };
        }
     if (( sum % var y == 0 )) {
        return true;
    }
     else{
        return false;
    }
}
var a = { 2 , 3 , 4 , 9 , 10 };
var x = 13;
if (check ( a , x )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
