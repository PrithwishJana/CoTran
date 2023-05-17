public void possibleways ( n ) {
    if (( n % var 2 == 1 )) {
        return 0 ;;
    }
     else if (( n % var 4 == 0 )){
        return n // 4 - 1 ;;
    }
    else{
        return n // 4 ;;
    }
}
var n = 20 ;;
System.out.println ( possibleways ( n ) ) ;;
