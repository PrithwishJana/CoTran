import collections;
import math;
import sys;
public void main ( ) {
    var n = int ( input ( ) );
    var a = list ( map ( int , input ( ) . split ( ) ) );
    var d = collections . defaultdict ( int );
    for (int x = 0; x < a.length; x++){
        var c = 0;
        while (x > 0) {
            c += x % 2;
            x //= 2;
        }
         d { c } += 1;
    }
    var ans = 0;
    for v in d . values ( ) :
        ans += v * ( v - 1 ) // 2;
    System.out.println ( ans );
}
if (var __name__ == "__main__") {
    var t = 1;
    while (t > 0) {
        main ( );
        t -= 1;
    }
}
  