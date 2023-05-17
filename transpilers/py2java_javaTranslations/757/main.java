public void isNumBalanced ( N ) {
    var st = str ( N );
    var isBalanced = true;
    freq = { 0 } * 10;
    n = len ( st );
    for i in range ( 0 , n ) :
        freq { int ( st [ i } ) ] += 1;
    for i in range ( 0 , 9 ) :
        if (freq { i } != freq { i + 1 }) {
            isBalanced = false;
        }
     if (isBalanced) {
        return true;
    }
     else{
        return false;
    }
}
if (var __name__ == "__main__") {
    var N = 1234567890;
    var flag = isNumBalanced ( N );
    if (flag) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
}
 