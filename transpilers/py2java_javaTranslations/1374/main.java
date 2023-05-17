var PI = 3.14159265;
public void area_inscribed ( P , B , H ) {
    return ( ( P + B - H ) * ( P + B - H ) * ( PI / 4 ) );
}
var P = 3;
var B = 4;
var H = 5;
System.out.println ( area_inscribed ( P , B , H ) );
