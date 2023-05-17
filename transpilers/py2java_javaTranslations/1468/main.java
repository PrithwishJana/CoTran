var sentence = input ( );
start , var letter = - 1 , str ( );
while (true) {
    if (( sentence { start } != ' ' ) and ( sentence { start } != '?' )) {
        letter = sentence { start };
        break;
    }
     start -= 1;
}
 if (letter . lower ( ) in { 'a' , 'e' , 'i' , 'o' , 'u' , 'y' }) {
    System.out.println ( 'YES' );
 }
 else{
    System.out.println ( 'NO' );
}
