public void increaseInVol ( l , b , h ) {
    var percentInc = ( ( 1 + ( l / 100 ) ) * ( 1 + ( b / 100 ) ) * ( 1 + ( h / 100 ) ) );
    percentInc -= 1;
    percentInc *= 100;
    return percentInc;
}
var l = 50;
var b = 20;
var h = 10;
System.out.println ( increaseInVol ( l , b , h ) , "%" );
