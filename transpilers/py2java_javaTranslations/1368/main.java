public void findNumber ( N , S ) {
    var i = ( ( ( N ) * ( N + 1 ) ) / 4 ) - ( ( S + 1 ) / 2 ) ;;
    return i ;;
}
public void check ( N , S ) {
    i = findNumber ( N , S ) ;;
    var integerI = int ( i ) ;;
    if (( i - integerI == 0 )) {
        System.out.println ( "Yes:" , integerI , "," , integerI + 1 ) ;;
    }
     else{
        System.out.println ( "No" ) ;;
    }
}
if (var __name__ == "__main__") {
    var N = 4 ;;
    S = 3 ;;
    check ( N , S ) ;;
    N = 5 ;;
    var S = 3 ;;
    check ( N , S ) ;;
}
 