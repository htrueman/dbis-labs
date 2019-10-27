$( "#update" ).click(function( event ) {
  const form = $('#form');
  $.ajax({
    type: 'put',
    data: form.serialize(),
    success: function(result) {
        window.location.replace("/users/");
    },
    error: function (err) {
      alert(err);
    }
  });
});


function deleteUser(id) {
  $.ajax({
    type: 'delete',
    success: function(result) {
        window.location.replace("/users/");
    },
    error: function (err) {
      alert(err);
    }
  });
}