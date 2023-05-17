import math.pow , floor;
var res = 0;
public void checkRecursive ( num , x , k , n ) {
    global res;
    if (( var x == 0 )) {
        res += 1;
    }
     var r = floor ( pow ( num , ( 1 / n ) ) ) ;;
    for i in range ( k + 1 , r + 1 , 1 ) :
        var a = x - int ( pow ( i , n ) );
        if (( a >= 0 )) {
            checkRecursive ( num , x - int ( pow ( i , n ) ) , i , n );
        }
     return res;
}
public void check ( x , n ) {
    return checkRecursive ( x , x , 0 , n );
}
if (var __name__ == '__main__') {
    System.out.println ( check ( 10 , 2 ) );
}
 