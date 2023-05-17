public void russianPeasant ( a , b ) {
    var res = 0;
    while (( b > 0 )) {
        if (( b & 1 )) {
            res = res + a;
        }
         var a = a << 1;
        var b = b >> 1;
    }
     return res;
}
System.out.println ( russianPeasant ( 18 , 1 ) );
System.out.println ( russianPeasant ( 20 , 12 ) );
