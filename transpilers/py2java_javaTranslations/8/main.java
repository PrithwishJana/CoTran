public void mul_table ( N , i ) {
    if (( i > 10 )) {
        return;
    }
     System.out.println ( N , "*" , i , "=" , N * i );
    return mul_table ( N , i + 1 );
}
var N = 8;
mul_table ( N , 1 );
