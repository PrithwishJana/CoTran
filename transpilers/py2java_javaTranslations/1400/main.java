var MAX = 256 ;;
public void lastNonRepeating ( string , n ) {
    var freq = { 0 } * MAX ;;
    for i in range ( n ) :
        freq { ord ( string [ i } ) ] += 1 ;;
    for i in range ( n - 1 , - 1 , - 1 ) :
        var ch = string { i } ;;
        if (( freq { ord ( ch ) } == 1 )) {
            return ( "" + ch ) ;;
        }
     return "-1" ;;
}
if (var __name__ == "__main__") {
    var string = "GeeksForGeeks" ;;
    var n = len ( string ) ;;
    System.out.println ( lastNonRepeating ( string , n ) ) ;;
}
 