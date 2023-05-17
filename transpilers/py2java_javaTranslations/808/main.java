public void XandYandZintercept ( A , B , C , D ) {
    var x = - D / A;
    var y = - D / B;
    var z = - D / C;
    return { x , y , z };
}
var A = 2;
var B = 5;
var C = 7;
var D = 8;
System.out.println ( XandYandZintercept ( A , B , C , D ) );
