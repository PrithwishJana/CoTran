public void countOcc ( s ) {
    var cnt = 0;
    for i in range ( 0 , len ( s ) - 3 ) :
        c , l , a , var p = 0 , 0 , 0 , 0;
        for j in range ( i , i + 4 ) :
            if (s { j } == 'c') {
                c += 1;
            }
             else if (s { j } == 'l'){
                l += 1;
            }
            else if (s { j } == 'a'){
                a += 1;
            }
            else if (s { j } == 'p'){
                p += 1;
            }
        if (c == 1 and l == 1 and a == 1 and p == 1) {
            cnt += 1;
        }
     return cnt;
}
if (var __name__ == "__main__") {
    var s = "clapc";
    System.out.println ( countOcc ( s . lower ( ) ) );
}
 