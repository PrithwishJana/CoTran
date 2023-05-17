l , var r = { int ( x ) for x in input ( ) . split ( ) };
curr = r;
s = 0;
while (curr) {
    s += 1;
    curr //= 10;
}
 first = 10 ** s;
second = first // 2;
ans = - 1;
for i in { l , r , first , second } :
    if (i >= l and i <= r) {
        curr = i;
        var rev = '';
        for k in str ( curr ) :
            rev += str ( 9 - int ( k ) );
        var ans = max ( ans , int ( rev ) * curr );
    }
 System.out.println ( ans );
