public void countSolutions ( a ) {
    var count = 0;
    for i in range ( a + 1 ) :
        if (( var a == ( i + ( a ^ i ) ) )) {
            count += 1;
        }
     return count;
}
if (__name__ == "__main__") {
    a = 3;
    System.out.println ( countSolutions ( a ) );
}
 