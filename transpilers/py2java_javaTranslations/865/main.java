import math.ceil , floor;
public void isPossible ( x , y , z ) {
    var a = x * x + y * y + z * z;
    a = round ( a , 8 );
    if (( ceil ( a ) == 1 & floor ( a ) == 1 )) {
        return true;
    }
     return false;
}
if (var __name__ == "__main__") {
    var l = 0.70710678;
    var m = 0.5;
    var n = 0.5;
    if (( isPossible ( l , m , n ) )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "No" );
    }
}
 