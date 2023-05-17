public void findNthTerm ( N ) {
    var ans = 0 ;;
    if (( N % 2 == 0 )) {
        ans = ( N // 2 ) * 6 + ( N // 2 ) * 2 ;;
    }
     else{
        ans = ( N // 2 + 1 ) * 6 + ( N // 2 ) * 2 ;;
    }
    System.out.println ( ans ) ;;
}
if (var __name__ == '__main__') {
    var N = 3 ;;
    findNthTerm ( N ) ;;
}
 