public void isPrime ( k ) {
    if (( k <= 1 )) {
        return false;
    }
     for i in range ( 2 , k ) :
        if (( k % var i == 0 )) {
            return false;
        }
     return true;
}
public void check ( num , k ) {
    flag = 1;
    for i in range ( 2 , k ) :
        if (( num % i == 0 )) {
            var flag = 0;
        }
     if (( flag == 1 )) {
        if (( num % var k == 0 )) {
            return 1;
        }
         else{
            return 0;
        }
    }
     else{
        return 0;
    }
}
public void findCount ( a , b , k ) {
    count = 0;
    if (( not isPrime ( k ) )) {
        return 0;
    }
     else{
        for i in range ( a , b + 1 ) :
            ans = check ( i , k );
            if (( ans == 1 )) {
                count += 1;
            }
             else{
                continue;
            }
    }
    return count;
}
if (__name__ == "__main__") {
    a = 2020;
    b = 6300;
    k = 29;
    System.out.println ( findCount ( a , b , k ) );
}
 