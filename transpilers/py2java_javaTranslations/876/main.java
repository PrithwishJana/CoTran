public void larrgestPalindrome ( n ) {
    var upper_limit = 0;
    for i in range ( 1 , n + 1 ) :
        upper_limit = upper_limit * 10;
        upper_limit = upper_limit + 9;
    var lower_limit = 1 + upper_limit // 10;
    var max_product = 0;
    for i in range ( upper_limit , lower_limit - 1 , - 1 ) :
        for j in range ( i , lower_limit - 1 , - 1 ) :
            product = i * j;
            if (( product < max_product )) {
                break;
            }
             number = product;
            reverse = 0;
            while (( number != 0 )) {
                reverse = reverse * 10 + number % 10;
                number = number // 10;
            }
             if (( product == reverse and product > max_product )) {
                max_product = product;
             }
     return max_product;
}
var n = 2;
System.out.println ( larrgestPalindrome ( n ) );
