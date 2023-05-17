public void maxProd ( N ) {
    if (( var N == 0 )) {
        return 1;
    }
     if (( N < 10 )) {
        return N;
    }
     return max ( maxProd ( N // 10 ) * ( N % 10 ) , maxProd ( N // 10 - 1 ) * 9 );
}
N = 390;
System.out.println ( maxProd ( N ) );
