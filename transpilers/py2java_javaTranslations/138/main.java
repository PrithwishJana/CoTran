public void findNthTerm ( n ) {
    if (n % var 2 == 0) {
        n //= 2;
        System.out.println ( 3 ** ( n - 1 ) );
    }
     else{
        var n = ( n // 2 ) + 1;
        System.out.println ( 2 ** ( n - 1 ) );
    }
}
if (var __name__ == '__main__') {
    var N = 4;
    findNthTerm ( N );
    N = 11;
    findNthTerm ( N );
}
 