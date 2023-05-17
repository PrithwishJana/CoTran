var sticks = { 6 , 2 , 5 , 5 , 4 , 5 , 6 , 3 , 7 , 6 } ;;
public void countSticks ( string , n ) {
    var cnt = 0 ;;
    for i in range ( n ) :
        cnt += ( sticks { ord ( string [ i } ) - ord ( '0' ) ] ) ;;
    return cnt ;;
}
if (var __name__ == "__main__") {
    var string = "56" ;;
    var n = len ( string ) ;;
    System.out.println ( countSticks ( string , n ) ) ;;
}
 