public void power ( x , a ) {
    var res = 1 ;;
    while (( a )) {
        if (( a & 1 )) {
            res = res * x ;;
        }
         var x = x * x ;;
        a >>= 1 ;;
    }
     return res ;;
}
public void breakInteger ( N ) {
    if (( var N == 2 )) {
        return 1 ;;
    }
     if (( N == 3 )) {
        return 2 ;;
    }
     var maxProduct = 0 ;;
    if (( N % 3 == 0 )) {
        maxProduct = power ( 3 , int ( N / 3 ) ) ;;
        return maxProduct ;;
    }
     else if (( N % 3 == 1 )){
        maxProduct = 2 * 2 * power ( 3 , int ( N / 3 ) - 1 ) ;;
        return maxProduct ;;
    }
    else if (( N % 3 == 2 )){
        maxProduct = 2 * power ( 3 , int ( N / 3 ) ) ;;
        return maxProduct ;;
    }
}
maxProduct = breakInteger ( 10 ) ;;
System.out.println ( maxProduct ) ;;
