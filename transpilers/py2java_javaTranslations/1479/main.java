public void findNthOccur ( string , ch , N ) {
    var occur = 0 ;;
    for i in range ( len ( string ) ) :
        if (( string { i } == ch )) {
            occur += 1 ;;
        }
         if (( occur == N )) {
            return i ;;
        }
     return - 1 ;;
}
if (var __name__ == "__main__") {
    var string = "geeks" ;;
    var ch = 'e' ;;
    var N = 2 ;;
    System.out.println ( findNthOccur ( string , ch , N ) ) ;;
}
 