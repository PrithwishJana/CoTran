public void xorCalc ( k ) {
    if (( var k == 1 )) {
        return 2;
    }
     if (( ( ( k + 1 ) & k ) == 0 )) {
        return k / 2;
    }
     return 1 ;;
}
k = 31;
System.out.println ( int ( xorCalc ( k ) ) );
