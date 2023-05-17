public void MinDeletion ( a , n ) {
    var map = dict . fromkeys ( a , 0 ) ;;
    for i in range ( n ) :
        map { a [ i } ] += 1 ;;
    var ans = 0 ;;
    for key , value in map . items ( ) :
        var x = key ;;
        var frequency = value ;;
        if (( x <= frequency )) {
            ans += ( frequency - x ) ;;
        }
         else{
            ans += frequency ;;
        }
    return ans ;;
}
if (var __name__ == "__main__") {
    var a = { 2 , 3 , 2 , 3 , 4 , 4 , 4 , 4 , 5 } ;;
    var n = len ( a ) ;;
    System.out.println ( MinDeletion ( a , n ) ) ;;
}
 