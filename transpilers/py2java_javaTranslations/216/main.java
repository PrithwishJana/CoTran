public void findWeights ( X ) {
    var sum = 0;
    power = 0;
    while (( sum < X )) {
        sum = pow ( 3 , power + 1 ) - 1;
        sum //= 2;
        power += 1;
    }
     var ans = 1;
    for i in range ( 1 , power + 1 ) :
        System.out.println ( ans , end = " " );
        ans = ans * 3;
}
var X = 2;
findWeights ( X );
