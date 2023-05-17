var PI = 3.14;
import math.pow , sqrt;
public void find_area ( r , d ) {
    var R = d / PI;
    R += pow ( r , 2 );
    R = sqrt ( R );
    var area = PI * pow ( R , 2 );
    return area;
}
if (var __name__ == '__main__') {
    var r = 4;
    var d = 5;
    System.out.println ( find_area ( r , d ) );
}
 