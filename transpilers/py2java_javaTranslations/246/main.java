public void countOfLetters ( string ) {
    var letter = 0 ;;
    for i in range ( len ( string ) ) :
        if (( ( string { i } >= 'A' and string { i } <= 'Z' ) or ( string { i } >= 'a' and string { i } <= 'z' ) )) {
            letter += 1 ;;
        }
     return letter ;;
}
public void countOfNumbers ( string ) {
    var number = 0 ;;
    for i in range ( len ( string ) ) :
        if (( string { i } >= '0' and string { i } <= '9' )) {
            number += 1 ;;
        }
     return number ;;
}
public void check ( string ) {
    if (( countOfLetters ( string ) == countOfNumbers ( string ) )) {
        System.out.println ( "Yes" ) ;;
    }
     else{
        System.out.println ( "No" ) ;;
    }
}
if (var __name__ == "__main__") {
    var string = "GeeKs01324" ;;
    check ( string ) ;;
}
 