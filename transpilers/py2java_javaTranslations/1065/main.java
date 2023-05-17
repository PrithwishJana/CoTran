public void findPosition ( k , n ) {
    var f1 = 0;
    f2 = 1;
    i = 2 ;;
    while (i != 0) {
        f3 = f1 + f2 ;;
        f1 = f2 ;;
        var f2 = f3 ;;
        if (f2 % var k == 0) {
            return n * i;
        }
         i += 1;
    }
     return;
}
n = 5 ;;
k = 4 ;;
System.out.println ( "Position of n'th multiple of k in Fibonacci Series is" , findPosition ( k , n ) ) ;;
