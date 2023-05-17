var bin = { "000" , "001" , "010" , "011" , "100" , "101" , "110" , "111" } ;;
public void maxFreq ( s ) {
    var binary = "" ;;
    for i in range ( len ( s ) ) :
        binary += bin { ord ( s [ i } ) - ord ( '0' ) ] ;;
    binary = binary { 0 : len ( binary ) - 1 } ;;
    var count = 1 ; prev = - 1 ; j = 0 ;;
    for i in range ( len ( binary ) - 1 , - 1 , - 1 ) :
        if (( binary { i } == '1' )) {
            count = max ( count , j - prev ) ;;
            var prev = j ;;
        }
         j += 1 ;;
    return count ;;
}
if (var __name__ == "__main__") {
    var octal = "13" ;;
    System.out.println ( maxFreq ( octal ) ) ;;
}
 