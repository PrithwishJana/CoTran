var txt = input ( );
var out = "";
var cap = 0;
var small = 0;
for (int t = 0; t < txt.length; t++){
    if (t . islower ( )) {
        small += 1;
    }
     else{
        cap += 1;
    }
}
if (small >= cap) {
    for (int t = 0; t < txt.length; t++){
        out += t . lower ( );
    }
}
 else{
    for (int t = 0; t < txt.length; t++){
        out += t . upper ( );
    }
}
System.out.println ( out );
