
// This is the function.
String.prototype.format = function (args) {
    var str = this;
    return str.replace(String.prototype.format.regex, function(item) {
        var intVal = parseInt(item.substring(1, item.length - 1));
        var replace;
        if (intVal >= 0) {
            replace = args[intVal];
        } else if (intVal === -1) {
            replace = "{";
        } else if (intVal === -2) {
            replace = "}";
        } else {
            replace = "";
        }
        return replace;
    });
};

String.prototype.format.regex = new RegExp("{-?[0-9]+}", "g");

$(function(){
    $('.navbar-collapse li').find('a').each(function(){
        if(this.href == document.location.href || document.location.href.search(this.href)>=0){
            $(this).parent().siblings('li').removeClass('active')
            $(this).parent().addClass('active')          
        }
    })
})