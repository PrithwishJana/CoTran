public void getPairs ( a ) {
    var count = 0;
    for i in range ( len ( a ) ) :
        for j in range ( len ( a ) ) :
            if (( a { i } < a { j } )) {
                count += 1;
            }
     return count;
}
if (var __name__ == "__main__") {
    var a = { 2 , 4 , 3 , 1 };
    System.out.println ( getPairs ( a ) );
}
 