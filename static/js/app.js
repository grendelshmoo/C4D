  function initPage(){
	   $("#id_document_date_range").hide();
     $('#id_recording_date_range').hide();
  }

  function ddRange() {
    var value = $('input[name=dd_sel]:checked').val();

    if (value === 'dd_range') {
      if($('#id_document_date_range').is(':hidden')) {
        $('#id_document_date_range').show();
      } else {
        $('#id_document_date_range').hide();
      }
    } else {
      $('#id_document_date_range').hide();
    }
  }

  function rdRange() {
    var value = $('input[name=rd_sel]:checked').val()

    if (value === 'rd_range') {
      if($('#id_recording_date_range').is(':hidden')) {
        $('#id_recording_date_range').show();
      } else {
        $('#id_recording_date_range').hide();
      }
    } else {
      $('#id_recording_date_range').hide();
    }
  }

  $(document).ready(function() { initPage(); });
