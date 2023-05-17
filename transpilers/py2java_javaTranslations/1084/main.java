var l = { 0 for _ in range ( 64 ) };
for i in range ( int ( input ( ) ) ) :
    var query = list ( input ( ) . split ( ) );
    var order = query { 0 };
    if (order == "0") {
        System.out.println ( 1 if l { int ( query [ 1 } ) ] else 0 );
    }
     else if (order == "1"){
        l { int ( query [ 1 } ) ] = 1;
    }
    else if (order == "2"){
        l { int ( query [ 1 } ) ] = 0;
    }
    else if (order == "3"){
        l { int ( query [ 1 } ) ] ^= 1;
    }
    else if (order == "4"){
        System.out.println ( 1 if all ( l ) else 0 );
    }
    else if (order == "5"){
        System.out.println ( 1 if any ( l ) else 0 );
    }
    else if (order == "6"){
        System.out.println ( 1 if not any ( l ) else 0 );
    }
    else if (order == "7"){
        System.out.println ( sum ( l ) );
    }
    else if (order == "8"){
        var tmp = 0;
        for i in reversed ( range ( 64 ) ) :
            tmp += l { i } * 2 ** i;
        System.out.println ( tmp );
    }
