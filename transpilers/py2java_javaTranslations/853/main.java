public void countCubes ( a , b ) {
    var cnt = 0;
    for i in range ( a , b + 1 ) :
        for j in range ( i + 1 ) :
            if (j * j * j > i) {
                break;
            }
             if (j * j * var j == i) {
                cnt += 1;
            }
     return cnt;
}
if (var __name__ == '__main__') {
    var a = 7;
    var b = 30;
    System.out.println ( "Count of Cubes is " , countCubes ( a , b ) );
}
 