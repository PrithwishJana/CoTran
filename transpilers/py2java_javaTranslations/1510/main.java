public void sum ( n ) {
    if (( var n == 1 )) {
        return 2 ;;
    }
     else{
        return ( n * ( n + 1 ) + sum ( n - 1 ) ) ;;
    }
}
n = 2 ;;
System.out.println ( sum ( n ) ) ;;
