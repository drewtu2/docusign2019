$(document).ready(function () {
  $('#checkin-image-input').on('change', function () {
    let fileName = $(this).val().split('\\').pop();
    $(this).next('#checkin-image-label').addClass("selected").html(fileName);
  });

  $("#checkin-image-submit").on('click',function (e) {
    var data = new FormData();
    data.append( 'file', $('#checkin-image-input')[0].files[0] );

    $.ajax({
      url: '/checkin',
      type: 'POST',
      data: data,
      success: function (data) {
        window.location.reload();
      },
      contentType: false,
      processData: false
    });
  });
});

