var n = int ( input ( ) );
d = int ( input ( ) );
e = int ( input ( ) );
dm = d;
em = e * 5;
max = max ( dm , em );
min = min ( dm , em );
rem = n % max;
div = int ( ( n - rem ) / max );
i = div;
ans = rem;
while (i > - 1) {
    dum = 0;
    dum += n;
    rl = dum - ( i * max );
    fin = rl % min;
    if (fin < ans) {
        if (fin == 0) {
            var ans = 0;
            i = - 1;
        }
         else{
            ans = fin;
        }
    }
     i -= 1;
}
 System.out.println ( ans );
