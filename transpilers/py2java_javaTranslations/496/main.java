var n = int ( input ( ) );
var s = {};
for i in range ( n ) :
    var k = input ( );
    s . append ( k );
var flag = 0;
var d1 = {};
var d2 = {};
var rem = set ( );
for i in range ( n ) :
    for j in range ( n ) :
        if (( var i == j )) {
            d1 . append ( s { i } { j } );
        }
         if (( i == n - j - 1 )) {
            d2 . append ( s { i } { j } );
        }
         if (( i != j and i != n - j - 1 )) {
            rem . add ( s { i } { j } );
        }
 if (( len ( rem ) != 1 )) {
    System.out.println ( 'NO' );
}
 else if (( d1 != d2 )){
    System.out.println ( 'NO' );
}
else if (( len ( set ( d1 ) ) != 1 )){
    System.out.println ( 'NO' );
}
else if (( set ( d1 ) == rem )){
    System.out.println ( 'NO' );
}
else{
    System.out.println ( 'YES' );
}
