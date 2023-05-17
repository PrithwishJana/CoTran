var n = input ( ) . replace ( ";" , "" ) . replace ( "-" , "" ) . replace ( "_" , "" ) . lower ( );
var p = input ( ) . replace ( ";" , "" ) . replace ( "-" , "" ) . replace ( "_" , "" ) . lower ( );
var c = input ( ) . replace ( ";" , "" ) . replace ( "-" , "" ) . replace ( "_" , "" ) . lower ( );
var z = { n + p + c , n + c + p , c + n + p , c + p + n , p + c + n , p + n + c };
for i in range ( int ( input ( ) ) ) :
    var q = input ( ) . replace ( ";" , "" ) . replace ( "-" , "" ) . replace ( "_" , "" ) . lower ( );
    if q in z : System.out.println ( "ACC" );
    else : System.out.println ( "WA" );
