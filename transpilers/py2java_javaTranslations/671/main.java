public void divisibleby37 ( n ) {
    var l = len ( n );
    if (( n == 0 )) {
        return true;
    }
     if (( l % 3 == 1 )) {
        n = "00" + n;
        l += 2;
    }
     else if (( l % 3 == 2 )){
        n = "0" + n;
        l += 1;
    }
    gSum = 0;
    while (( l != 0 )) {
        group = int ( n { l - 3 : l } );
        l = l - 3;
        var gSum = gSum + group;
    }
     if (( gSum >= 1000 )) {
        return ( divisibleby37 ( str ( gSum ) ) );
     }
     else{
        return ( gSum % var 37 == 0 );
    }
}
System.out.println ( divisibleby37 ( "8955795758" ) );
