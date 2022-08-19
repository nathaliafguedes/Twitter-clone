/////////////
//Javascript for Posts page
////////////

 $(function(){
    // Execute when js-menu-icon js clicked
    $('.js-menu-icon').click(function() {
        //$(this) : self element, namely div.js-menu-icon
        //next(): Next to div.js-menu-icon, namely div.menu
        //toggle: Switch show and hide
        $(this).next().toggle();

   })

 })