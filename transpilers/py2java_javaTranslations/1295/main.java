var num = int ( input ( ) );
num = input ( );
var list_is = {};
for (int i = 0; i < num.length; i++){
    list_is . append ( int ( i ) );
}
var list_is1 = list_is { : len ( list_is ) // 2 };
var list_is2 = list_is { len ( list_is ) // 2 : };
var sum1 = sum ( list_is1 );
sum2 = sum ( list_is2 );
condition = false;
for (int i = 0; i < list_is.length; i++){
    if (i == 4 or i == 7) {
        condition = true;
        continue;
    }
     else{
        condition = false;
        break;
    }
}
if (condition == true) {
    if (sum1 == sum2) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
}
 else{
    System.out.println ( "NO" );
}
