public void sumDivisibles ( A , B , M ) {
    var sum = 0;
    for i in range ( A , B + 1 ) :
        if (( i % var M == 0 )) {
            sum += i;
        }
     return sum;
}
if (__name__ == "__main__") {
    A = 6;
    B = 15;
    M = 3;
    System.out.println ( sumDivisibles ( A , B , M ) );
}
 