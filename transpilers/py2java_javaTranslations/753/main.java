var ip = input ( );
st = "";
if (len ( ip ) != 1) {
    if (ip { 0 } == "9") {
        st = "9";
        ip = ip { 1 : };
    }
     for (int i = 0; i < ip.length; i++){
        if (int ( i ) > 4) {
            var n = 9 - int ( i );
            st += str ( n );
        }
         else{
            st += i;
        }
     }
}
 else{
    var st = ip;
}
System.out.println ( int ( st ) );
