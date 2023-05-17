public void findTime ( T , K ) {
    var minutes = ( ( ( ord ( T { 0 } ) - ord ( '0' ) ) * 10 + ord ( T { 1 } ) - ord ( '0' ) ) * 60 + ( ( ord ( T { 3 } ) - ord ( '0' ) ) * 10 + ord ( T { 4 } ) - ord ( '0' ) ) ) ;;
    minutes += K;
    var hour = ( int ( minutes / 60 ) ) % 24;
    var min = minutes % 60;
    if (( hour < 10 )) {
        System.out.println ( "0" + str ( hour ) + ":" , var end = "" );
    }
     else{
        System.out.println ( str ( hour ) + ":" , end = "" );
    }
    if (( min < 10 )) {
        System.out.println ( "0" + str ( min ) );
    }
     else{
        System.out.println ( str ( min) );
    }
}
if (var __name__ == '__main__') {
    var T = "21:39";
    var K = 43;
    findTime ( T , K );
}
 