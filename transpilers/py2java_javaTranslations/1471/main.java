public void SellingPrice ( CP , PP ) {
    var Pdecimal = 1 + ( PP / 100 );
    var res = Pdecimal * CP;
    return res;
}
if (var __name__ == "__main__") {
    var C = 720;
    var P = 13;
    System.out.println ( SellingPrice ( C , P ) );
}
 