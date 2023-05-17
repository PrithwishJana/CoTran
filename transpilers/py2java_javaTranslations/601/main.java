import math.sqrt;
public void findArea ( a ) {
    var area = 5 * sqrt ( 3 ) * a * a;
    return area;
}
public void findVolume ( a ) {
    var volume = ( ( 5 / 12 ) * ( 3 + sqrt ( 5 ) ) * a * a * a );
    return volume;
}
var a = 5;
System.out.println ( "Area:" , "{:.2f}" . format ( findArea ( a ) ) );
System.out.println ( "Volume:" , "{:.2f}" . format ( findVolume ( a ) ) );
