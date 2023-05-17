public void System.out.printlnSeriesSum ( N ) {
    var sum = 0 ;;
    var a = 1 ;;
    cnt = 0 ;;
    flag = true ;;
    sum += a ;;
    while (( cnt < N )) {
        nextElement = None ;;
        if (( flag )) {
            nextElement = a * 2 ;;
            sum += nextElement ;;
            flag = not flag ;;
        }
         else{
            nextElement = a * ( 3 / 2 ) ;;
            sum += nextElement ;;
            flag = not flag ;;
        }
        a = nextElement ;;
        cnt += 1;
    }
     System.out.println ( sum ) ;;
}
if (var __name__ == "__main__") {
    var N = 8 ;;
    System.out.printlnSeriesSum ( N ) ;;
}
 