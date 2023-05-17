var dic = {};
var S = list ( input ( ) );
for (int s = 0; s < S.length; s++){
    if s not in dic : dic { s } = 1;
    else : dic { s } += 1;
}
var ans = 0;
for k in list ( dic . keys ( ) ) :
    if dic { k } & 1 : ans += 1;
System.out.println ( ans >> 1 );
