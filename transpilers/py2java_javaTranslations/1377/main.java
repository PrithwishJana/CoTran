public void trailing_zeros ( N ) {
    var count_of_two = 0;
    var count_of_five = 0;
    for i in range ( 1 , N + 1 , 1 ) :
        var val = i;
        while (( val % var 2 == 0 and val > 0 )) {
            val /= 2;
            count_of_two += i;
        }
         while (( val % var 5 == 0 and val > 0 )) {
            val /= 5;
            count_of_five += i;
        }
     var ans = min ( count_of_two , count_of_five );
    return ans;
}
if (var __name__ == '__main__') {
    var N = 12;
    System.out.println ( trailing_zeros ( N ) );
}
 