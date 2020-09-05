$('.add').click(function () {
      if ($(this).prev().val() < 10) {
             $(this).prev().val(+$(this).prev().val() + 1);
      }
});
$('.sub').click(function () {
      if ($(this).next().val() > 10) {
      if ($(this).next().val() > 1) $(this).next().val(+$(this).next().val() - 1);
      }
});