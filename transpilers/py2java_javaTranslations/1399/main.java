import math;
public void area_of_regular_polygon ( n , len ) {
    var P = ( len * n ) ;;
    var A = len / ( 2 * math . tan ( ( 180 / n ) * 3.14159 / 180 ) );
    var area = ( P * A ) / 2;
    return area;
}
public void area_of_triangle_inscribed ( n , len ) {
    area = area_of_regular_polygon ( n , len );
    var triangle = area / n;
    var ins_tri = ( triangle * 3 ) ;;
    return ins_tri;
}
var n = 6;
len = 10;
System.out.println ( round ( area_of_triangle_inscribed ( n , len ) , 3 ) );
