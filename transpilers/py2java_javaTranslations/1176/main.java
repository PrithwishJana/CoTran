public void calculate_sum ( a , N ) {
    var m = N / a;
    sum = m * ( m + 1 ) / 2;
    var ans = a * sum;
    System.out.println ( "Sum of multiples of " , a , " up to " , N , " = " , ans );
}
calculate_sum ( 7 , 49 );
