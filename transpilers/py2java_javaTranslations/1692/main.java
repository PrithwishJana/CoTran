public void sum ( k , n ) {
    var sum = ( pow ( k , n + 1 ) - pow ( k - 1 , n + 1 ) ) ;;
    return sum ;;
}
var n = 3 ;;
var K = 3 ;;
System.out.println ( sum ( K , n ) ) ;;
