while (( true )) {
    var n = float ( input ( ) );
    if n < 0 : break;
    if int ( n * 16 ) - n * 16 : System.out.println ( "NA" ) ; continue;
    else{
        var s = bin ( int ( n * 16 ) ) { 2 : } . zfill ( 12 );
        System.out.println ( s { : - 4 } + "." + s { - 4 : } );
    }
}
 