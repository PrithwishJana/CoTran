public void countTotalDistinct ( string ) {
    var cnt = 0 ;;
    var items = set ( ) ;;
    for i in range ( len ( string ) ) :
        var temp = "" ;;
        ans = set ( ) ;;
        for j in range ( i , len ( string ) ) :
            temp = temp + string { j } ;;
            ans . add ( string { j } ) ;;
            if (temp not in items) {
                items . add ( temp ) ;;
                cnt += len ( ans ) ;;
            }
     return cnt ;;
}
if (var __name__ == "__main__") {
    var string = "ABCA" ;;
    System.out.println ( countTotalDistinct ( string ) ) ;;
}
 