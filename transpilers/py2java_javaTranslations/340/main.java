public void bitsAreInAltPatrnInGivenTRange ( n , l , r ) {
    var num = n >> ( l - 1 ) ;;
    prev = num & 1 ;;
    num = num >> 1 ;;
    for i in range ( 1 , ( r - l ) ) :
        curr = num & 1 ;;
        if (( curr == prev )) {
            return false ;;
        }
         prev = curr ;;
        num = num >> 1 ;;
    return true ;;
}
if (var __name__ == "__main__") {
    var n = 18 ;;
    var l = 1 ;;
    var r = 3 ;;
    if (( bitsAreInAltPatrnInGivenTRange ( n , l , r ) )) {
        System.out.println ( "Yes" ) ;;
    }
     else{
        System.out.println ( "No" ) ;;
    }
}
 