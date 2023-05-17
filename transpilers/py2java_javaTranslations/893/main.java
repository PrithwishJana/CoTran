public void countNumber ( N , S ) {
    var countElements = 0 ;;
    currentSum = 0;
    currSum = 0 ;;
    while (( currSum <= S )) {
        currSum += N ;;
        N = N - 1 ;;
        countElements = countElements + 1 ;;
    }
     return countElements ;;
}
var N = 5 ;;
var S = 11 ;;
var count = countNumber ( N , S ) ;;
System.out.println ( count ) ;;
