$(document).ready(function () {
   $('a.exercises').click(function (event) {
       event.preventDefault();
       $('div#exercises').show(500);
   });

   $('p.x').click(function (event) {
       event.preventDefault();
       $('div#exercises').hide(500);
   })

});