public void gcd ( a , b ) {
    if (var a == 0) {
        return b;
    }
     else{
        return gcd ( b % a , a );
    }
}
t = int ( input ( ) );
while (t) {
    t -= 1;
    a , b = map ( int , input ( ) . split ( ) );
    c = gcd ( a , b );
    a = a // c;
    b = b // c;
    if (a == b) {
        var ans1 = 1;
        ans2 = 0;
    }
     else if (a % 2 == 0 or b % 2 == 0){
        ans1 = 1;
        ans2 = 1;
    }
    else{
        ans1 = a * b // 2 + 1;
        var ans2 = a * b // 2;
    }
    System.out.println ( ans1 , ans2 );
}
 