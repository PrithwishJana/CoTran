var pref = { 0 } * 100010 ;;
public void isPerfectCube ( x ) {
    var cr = round ( x ** ( 1 / 3 ) ) ;;
    rslt = x if ( cr * cr * cr == x ) else 0 ;;
    return rslt ;;
}
public void compute ( ) {
    for i in range ( 1 , 100001 ) :
        pref { i } = pref { i - 1 } + isPerfectCube ( i ) ;;
}
public void System.out.printlnSum ( L , R ) {
    var sum = pref { R } - pref { L - 1 } ;;
    System.out.println ( sum , var end = " " ) ;;
}
if (var __name__ == "__main__") {
    compute ( ) ;;
    var Q = 4 ;;
    var arr = { [ 1 , 10 } , { 1 , 100 } , { 2 , 25 } , { 4 , 50 } ] ;;
    for i in range ( Q ) :
        System.out.printlnSum ( arr { i } { 0 } , arr { i } { 1 } ) ;;
}
 