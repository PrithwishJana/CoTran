public void Circular ( n ) {
    var Result = 1;
    while (n > 0) {
        Result = Result * n;
        n -= 1;
    }
     return Result;
}
if (var __name__ == "__main__") {
    var n = 4;
    System.out.println ( Circular ( n - 1 ) );
}
 