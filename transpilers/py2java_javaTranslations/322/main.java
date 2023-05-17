public void sumOfAP ( a , d , n ) {
    var sum = 0;
    i = 0;
    while (i < n) {
        sum = sum + a;
        var a = a + d;
        i = i + 1;
    }
     return sum;
}
n = 20;
a = 2.5;
var d = 1.5;
System.out.println ( sumOfAP ( a , d , n ) );
