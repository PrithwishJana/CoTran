public void findNth ( n ) {
    var count = 0 ;;
    curr = 19 ;;
    while (( true )) {
        sum = 0 ;;
        x = curr ;;
        while (( x > 0 )) {
            sum = sum + x % 10 ;;
            x = int ( x / 10 ) ;;
        }
         if (( sum == 10 )) {
            count += 1 ;;
         }
         if (( count == n )) {
            return curr ;;
        }
         curr += 9 ;;
    }
     return - 1 ;;
}
System.out.println ( findNth ( 5 ) ) ;;
