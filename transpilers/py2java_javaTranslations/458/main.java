var cnt = input ( );
for k in range ( int ( cnt ) ) :
    var ip = input ( );
    if (ip == "") {
        System.out.println ( "0000:0000:0000:0000:0000:0000:0000:0000" );
        continue;
    }
     ip = ip . split ( ":" );
    ret = "";
    if (ip { 0 } == "") {
        ip = { "0000" } * ( 8 - len ( ip ) + 2 ) + ip { 2 : };
    }
     else if (ip { - 1 } == ""){
        ip = ip { : - 2 } + { "0000" } * ( 8 - len ( ip ) + 2 );
    }
    for i in range ( len ( ip ) ) :
        if (ip { i } == "") {
            ip = ip { : i } + { "0000" } * ( 8 - len ( ip ) + 1 ) + ip { i + 1 : };
        }
     for i in range ( len ( ip ) ) :
        if (ip { i } != "") {
            ip { i } = "0" * ( 4 - len ( ip { i } ) ) + ip { i };
        }
     System.out.println ( ":" . join ( ip ) );
