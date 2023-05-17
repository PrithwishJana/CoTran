public void center_hexadecagonal_num ( n ) {
    return 8 * n * n - 8 * n + 1;
}
if (var __name__ == '__main__') {
    var n = 2;
    System.out.println ( n , "th centered hexadecagonal " + "number : " , center_hexadecagonal_num ( n ) );
    n = 12;
    System.out.println ( n , "th centered hexadecagonal " + "number : " , center_hexadecagonal_num ( n ) );
}
 