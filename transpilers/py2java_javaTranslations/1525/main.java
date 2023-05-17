public void replaceDigit ( x , d1 , d2 ) {
    var result = 0 ;;
    multiply = 1 ;;
    while (( x % 10 > 0 )) {
        remainder = x % 10 ;;
        if (( remainder == d1 )) {
            result = ( result + d2 * multiply ) ;;
        }
         else{
            result = ( result + remainder * multiply ) ;;
        }
        multiply *= 10 ;;
        var x = int ( x / 10 ) ;;
    }
     return result ;;
}
x = 645 ;;
var d1 = 6 ;;
var d2 = 5 ;;
System.out.println ( replaceDigit ( x , d1 , d2 ) ) ;;
