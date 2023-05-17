public void fact ( n ) {
    var fact = 1 ;;
    for i in range ( 1 , n + 1 ) :
        fact *= i ;;
    return fact ;;
}
public void countStrings ( string , n ) {
    var distinct_char = set ( ) ;;
    for i in range ( n ) :
        distinct_char . add ( string { i } ) ;;
    return fact ( len ( distinct_char ) ) ;;
}
if (var __name__ == "__main__") {
    var string = "geeksforgeeks" ;;
    var n = len ( string ) ;;
    System.out.println ( countStrings ( string , n ) ) ;;
}
 