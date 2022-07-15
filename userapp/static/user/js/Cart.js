$("#addtocart").click(function (e) {
  e.preventDefault();
  var productid = $(".prod_id").val();
 

  $.ajax({
    url: "",
    type: "POST",
    data: { product_id: $(".prod_id").val() },
    csrfmiddlewaretoken: "{{csrf_token}}",
    dataType: "json",
    success: function () {
      alert("added to cart");
    },
  });
  
});
