public void findSum ( n , a , b ) {
    var sum = 0;
    for i in range ( 0 , n , 1 ) :
        if (( i % var a == 0 or i % b == 0 )) {
            sum += i;
        }
     return sum;
}
if (__name__ == '__main__') {
    n = 10;
    a = 3;
    var b = 5;
    System.out.println ( findSum ( n , a , b ) );
}
 