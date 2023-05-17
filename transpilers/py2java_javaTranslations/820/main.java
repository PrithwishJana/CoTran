public void centered_heptagonal_num ( n ) {
    return ( 7 * n * n - 7 * n + 2 ) // 2;
}
var n = 5;
System.out.println ( "%sth Centered heptagonal number : " % n , centered_heptagonal_num ( n ) );
