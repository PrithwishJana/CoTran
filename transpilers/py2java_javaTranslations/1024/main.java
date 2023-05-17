var n = int ( input ( ) );
var a = sorted ( list ( map ( int , input ( ) . split ( ) ) ) );
if (( a { 0 } == a { - 1 } )) {
    var x = a . count ( a { 0 } ) * ( a . count ( a { - 1 } ) - 1 ) // 2;
}
 else{
    x = a . count ( a { 0 } ) * a . count ( a { - 1 } );
}
System.out.println ( a { - 1 } - a { 0 } , x );
