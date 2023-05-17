public void doublefactorial ( n ) {
    if (( var n == 0 or n == 1 )) {
        return 1 ;;
    }
     return n * doublefactorial ( n - 2 ) ;;
}
System.out.println ( "Double factorial is" , doublefactorial ( 5 ) ) ;;
