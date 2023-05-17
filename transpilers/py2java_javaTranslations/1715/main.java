public void findHypotenuse ( side1 , side2 ) {
    var h = ( ( ( side1 * side1 ) + ( side2 * side2 ) ) ** ( 1 / 2 ) ) ;;
    return h ;;
}
var side1 = 3 ;;
var side2 = 4 ;;
System.out.println ( findHypotenuse ( side1 , side2 ) ) ;;
