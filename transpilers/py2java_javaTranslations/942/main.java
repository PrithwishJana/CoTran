n , b , var d = list ( map ( int , input ( ) . split ( ) ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var waste = 0;
num = 0;
for (int i = 0; i < a.length; i++){
    if (i <= b) {
        waste += i;
    }
     if (waste > d) {
        num += 1;
        waste = 0;
    }
}
 System.out.println ( num );
