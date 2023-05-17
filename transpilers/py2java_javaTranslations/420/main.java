public void normalSieve ( n ) {
    var prime = { 0 } * int ( n / 2 ) ;;
    var i = 3 ;;
    while (( i * i < n )) {
        if (( prime { int ( i / 2 ) } == 0 )) {
            j = i * i ;;
            while (( j < n )) {
                prime { int ( j / 2 ) } = 1 ;;
                j += i * 2 ;;
            }
        }
          i += 2 ;;
    }
     System.out.println ( 2 , end = " " ) ;;
    i = 3 ;;
    while (( i < n )) {
        if (( prime { int ( i / 2 ) } == 0 )) {
            System.out.println ( i , var end = " " ) ;;
        }
         i += 2 ;;
    }
 }
if (var __name__ == '__main__') {
    var n = 100 ;;
    normalSieve ( n ) ;;
}
 