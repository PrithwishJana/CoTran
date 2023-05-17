var a = list ( map ( int , input ( ) . split ( ) ) );
da = a { 0 };
db = a { 1 };
if (da > db) {
    if (da == 9 and db == 1) {
        System.out.println ( 9 , 10 );
    }
     else{
        System.out.println ( - 1 );
    }
}
 else if (da == db){
    System.out.println ( str ( da ) + str ( 0 ) , str ( db ) + str ( 1 ) );
}
else{
    if (db - da != 1) {
        System.out.println ( - 1 );
    }
     else{
        System.out.println ( da , db );
    }
}
