public void productEqual ( n ) {
    if (n < 10) {
        return false;
    }
     var prodOdd = 1 ; prodEven = 1;
    while (n > 0) {
        digit = n % 10;
        prodOdd *= digit;
        n = n // 10;
        if (n == 0) {
            break ;;
        }
         digit = n % 10;
        prodEven *= digit;
        n = n // 10;
    }
     if (prodOdd == prodEven) {
        return true;
     }
     return false;
}
var n = 4324;
if (productEqual ( n )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
