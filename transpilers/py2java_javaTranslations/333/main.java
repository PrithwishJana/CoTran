public void nextPowerOf2 ( n ) {
    var count = 0;
    if (( n and not ( n and ( n - 1 ) ) )) {
        return n;
    }
     while (n != 0) {
        n >>= 1;
        count += 1;
    }
     return 1 << count;
}
public void removeElement ( n ) {
    if (var n == 1 or n == 2) {
        return 0;
    }
     a = nextPowerOf2 ( n );
    if (n == a or n == a - 1) {
        return 1;
    }
     else if (n == a - 2){
        return 0;
    }
    else if (n % 2 == 0){
        return 1;
    }
    else{
        return 2;
    }
}
if (__name__ == "__main__") {
    n = 5;
    System.out.println ( removeElement ( n ) );
}
 