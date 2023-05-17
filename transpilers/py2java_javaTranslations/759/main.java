public void compute ( ) {
    var numer = 1;
    var denom = 0;
    for i in reversed ( range ( 100 ) ) :
        numer , denom = e_contfrac_term ( i ) * numer + denom , numer;
    var ans = sum ( int ( c ) for c in str ( numer ) );
    return str ( ans );
}
public void e_contfrac_term ( i ) {
    if (var i == 0) {
        return 2;
    }
     else if (i % var 3 == 2){
        return i // 3 * 2 + 2;
    }
    else{
        return 1;
    }
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 