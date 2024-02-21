
const SQL = "SQL";

function what_is_flag(arg){
    console.warn("Non, pas ici non-plus.");
    console.warn("Parfois, il faut se perdre pour se retrouver. Un nouveau départ peut être le chemin vers la découverte de soi. - Ralph Waldo Emerson");

}

const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

function generateRandomString(length) {
    let result = '';
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
}


alasql("CREATE TABLE users (id string, password string, val string)");



for (let step = 0; step < 250; step++) {
    alasql(`INSERT INTO users VALUES ("user${step}", "${generateRandomString(7)}", "${generateRandomString(4)}")`);
  }
  
  alasql('INSERT INTO users VALUES ("FLAG", "{PostgreSQL}", "PAPU")');

  for (let step = 250; step < 331; step++) {
    alasql(`INSERT INTO users VALUES ("user${step}", "${generateRandomString(7)}", "${generateRandomString(4)}")`);
  }

function request(){
    sqlRequest = document.getElementById('sqlTable').value;

    const result = alasql(sqlRequest);
        


    alert('SQL Result:\n' + JSON.stringify(result, null, 2));

}


function validate(){
    const _0x383ff4=_0x5be5;function _0x5be5(_0x1808e5,_0x2f2ab2){const _0x20212e=_0x2021();return _0x5be5=function(_0x5be50c,_0x5e308a){_0x5be50c=_0x5be50c-0x148;let _0x4e03ca=_0x20212e[_0x5be50c];return _0x4e03ca;},_0x5be5(_0x1808e5,_0x2f2ab2);}function _0x2021(){const _0x3a1a3a=['3oERVlD','975540eCEmcI','value','212ZXWHRF','570270ogUYPC','10113540kiWmYD','96620WlKjBL','309760vcbOsU','href','119NuGOfl','location','7121016fxUyuh','PostgreSQL','714033xupYHU'];_0x2021=function(){return _0x3a1a3a;};return _0x2021();}(function(_0x5e3a62,_0x43efb1){const _0x16240d=_0x5be5,_0x35a397=_0x5e3a62();while(!![]){try{const _0x337f27=-parseInt(_0x16240d(0x14a))/0x1+-parseInt(_0x16240d(0x14f))/0x2*(parseInt(_0x16240d(0x14b))/0x3)+parseInt(_0x16240d(0x14e))/0x4*(-parseInt(_0x16240d(0x151))/0x5)+parseInt(_0x16240d(0x14c))/0x6+parseInt(_0x16240d(0x154))/0x7*(parseInt(_0x16240d(0x152))/0x8)+parseInt(_0x16240d(0x148))/0x9+parseInt(_0x16240d(0x150))/0xa;if(_0x337f27===_0x43efb1)break;else _0x35a397['push'](_0x35a397['shift']());}catch(_0x40a524){_0x35a397['push'](_0x35a397['shift']());}}}(_0x2021,0x92804));const useless='Flag123',flag='ThisisFLag';var s=document['getElementById']('sqlFlag')[_0x383ff4(0x14d)];s===_0x383ff4(0x149)?window[_0x383ff4(0x155)][_0x383ff4(0x153)]='../george_et_alfred':console['error']('Ce\x20n\x27est\x20pas\x20le\x20bon\x20flag\x20;(');
}
