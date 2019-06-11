$(document).ready(function () {
  thankyou();
  function thankyou(){
    if($('#thank_you').val() === "true"){
      $('#thankyoumodal').modal('show');
    }
  }
});