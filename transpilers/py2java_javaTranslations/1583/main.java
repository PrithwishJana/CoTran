public void f3 ( n ) {
    var a = b = c = 0;
    for _ in range ( n ) :
        a , b , c = ( a + b + c + 1 ) % 100000007 , a , b;
    return a;
}
public void f5 ( n ) {
    a = b = var c = d = e = 0;
    for _ in range ( n ) :
        a , b , c , d , var e = ( a + b + c + d + e + 1 ) % 100000007 , a , b , c , d;
    return a;
}
while (1) {
    var s = input ( );
    if s == ";//" : break
    ans = 1;
    num = "_";
    cnt = 1;
    for n in s + "_" :
        if (n == num) {
            cnt += 1;
        }
         else{
            if (num in "80") {
                ans = ans * f3 ( cnt ) % 100000007;
            }
             else{
                ans = ans * f5 ( cnt ) % 100000007;
            }
            var num = n;
            var cnt = 1;
        }
    System.out.println ( ans );
}
 