public void isPerfectCube ( x ) {
    var cr = int ( x ** ( 1 / 3 ) ) ;;
    return ( cr * cr * cr == x ) ;;
}
public void canBePerfectCube ( N , K ) {
    if (( isPerfectCube ( N + K ) or isPerfectCube ( N - K ) )) {
        System.out.println ( "Yes" ) ;;
    }
     else{
        System.out.println ( "No" ) ;;
    }
}
if (var __name__ == "__main__") {
    var N = 7 ; K = 1 ;;
    canBePerfectCube ( N , K ) ;;
    N = 5 ; K = 4 ;;
    canBePerfectCube ( N , K ) ;;
    N = 7 ; var K = 2 ;;
    canBePerfectCube ( N , K ) ;;
}
 