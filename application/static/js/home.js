$(document).ready(function() {
  $("#personal_new").on("click", function(event) {
    $("#add_personal_modal").modal({keyboard: true});
    var notes_quill = new Quill('#p_notes', {
      theme: 'snow'
    });
    var assumptions_quill = new Quill('#p_assumptions', {
      theme: 'snow'
    });
    var constraints_quill = new Quill('#p_constraints', {
      theme: 'snow'
    });
  });
});

$(document).ready(function() {
  $("#team_new").on("click", function(event) {
    $("#add_team_modal").modal({keyboard: true});
      var notes_quill = new Quill('#t_notes', {
        theme: 'snow'
      });
      var assumptions_quill = new Quill('#t_assumptions', {
        theme: 'snow'
      });
      var constraints_quill = new Quill('#t_constraints', {
        theme: 'snow'
      });
  });
});

$(function () {
  $('#due_date_calendar').datetimepicker({
    minDate: moment()
  });
});
