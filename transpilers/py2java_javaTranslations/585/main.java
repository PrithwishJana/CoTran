public void findAngle ( n ) {
    var interiorAngle = int ( ( n - 2 ) * 180 / n );
    var exteriorAngle = int ( 360 / n );
    System.out.println ( "Interior angle:" , interiorAngle );
    System.out.println ( "Exterior angle:" , exteriorAngle );
}
var n = 10;
findAngle ( n );
