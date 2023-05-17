var N = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var odd = 0;
var m2 = 0;
m4 = 0;
for (int n = 0; n < a.length; n++){
    if (n % 2 == 1) {
        odd += 1;
    }
     else if (n % 4 != 0){
        m2 += 1;
    }
    else{
        m4 += 1;
    }
}
if (m4 >= odd or ( m2 == 0 and m4 >= odd - 1 )) {
    System.out.println ( 'Yes' );
}
 else{
    System.out.println ( 'No' );
}
