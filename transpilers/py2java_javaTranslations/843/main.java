var s = input ( );
n = int ( input ( ) );
ans = 0;
for i in range ( n ) :
    x = input ( );
    a , b = 0 , 0;
    for (int j = 0; j < s.length; j++){
        if (j == x { 0 }) {
            a += 1;
        }
         else if (j == x { 1 }){
            b += 1;
        }
        else{
            ans = ans + min ( a , b );
            a , b = 0 , 0;
        }
    }
    ans = ans + min ( a , b );
System.out.println ( ans );
