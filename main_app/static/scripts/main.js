$(document).ready(function() {
    $(".nav-toggler").each(function(_, navToggler) {
      var target = $(navToggler).data("target");
      $(navToggler).on("click", function() {
        $(target).animate({
          height: "toggle"
        });
      });
    });
  });

$('.hidden').on('hover', function() {
  $(this).toggleClass('hidden').siblings().removeClass('hidden');
})

