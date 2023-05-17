public void pre_process ( substrings , s ) {
    var n = len ( s ) ;;
    for i in range ( n ) :
        var dup = "" ;;
        for j in range ( i , n ) :
            dup += s { j } ;;
            substrings . append ( dup ) ;;
    substrings . sort ( ) ;;
    return substrings ;;
}
if (var __name__ == "__main__") {
    var s = "geek" ;;
    substrings = {} ;;
    substrings = pre_process ( substrings , s ) ;;
    queries = { 1 , 5 , 10 } ;;
    var q = len ( queries ) ;;
    for i in range ( q ) :
        System.out.println ( substrings { queries [ i } - 1 ] ) ;;
}
 