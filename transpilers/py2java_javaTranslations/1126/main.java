public void maxZeros ( N ) {
    var maxm = - 1;
    cnt = 0;
    while (( N )) {
        if (( not ( N & 1 ) )) {
            cnt += 1;
            N >>= 1;
            maxm = max ( maxm , cnt );
        }
         else{
            maxm = max ( maxm , cnt );
            var cnt = 0;
            N >>= 1;
        }
    }
     return maxm;
}
var N = 14;
System.out.println ( maxZeros ( N ) );
