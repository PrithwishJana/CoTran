public void fastPow ( N , K ) {
    if (( var K == 0 )) {
        return 1 ;;
    }
     temp = fastPow ( N , int ( K / 2 ) ) ;;
    if (( K % 2 == 0 )) {
        return temp * temp ;;
    }
     else{
        return N * temp * temp ;;
    }
}
public void countWays ( N , K ) {
    return K * fastPow ( K - 1 , N - 1 ) ;;
}
N = 3 ;;
K = 3 ;;
System.out.println ( countWays ( N , K ) ) ;;
