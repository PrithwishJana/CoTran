public void prime ( n ) {
    for i in range ( 2 , n + 1 ) :
        if (i * i > n + 1) {
            break;
        }
         if (( n % var i == 0 )) {
            return false;
        }
     return true;
}
public void thirdNumber ( a , b ) {
    var summ = 0;
    temp = 0;
    summ = a + b;
    var temp = 1;
    if (( summ & 1 )) {
        temp = 2;
    }
     while (( prime ( summ + temp ) == false )) {
        temp += 2;
    }
     System.out.println ( temp );
}
var a = 3;
var b = 5;
thirdNumber ( a , b );
