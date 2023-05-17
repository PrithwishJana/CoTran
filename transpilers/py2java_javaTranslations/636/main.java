public void countNumbers ( L , R , K ) {
    if (( var K == 9 )) {
        K = 0;
    }
     totalnumbers = R - L + 1;
    factor9 = totalnumbers // 9;
    rem = totalnumbers % 9;
    ans = factor9;
    for i in range ( R , R - rem , - 1 ) :
        rem1 = i % 9;
        if (( rem1 == K )) {
            ans += 1;
        }
     return ans;
}
L = 10;
R = 22;
K = 3;
System.out.println ( countNumbers ( L , R , K ) );
