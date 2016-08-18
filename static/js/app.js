  function initPage(){
     $("tr:has(.dd-hidden)").hide();
     $("tr:has(.rd-hidden)").hide();
  }

  function ddRange() {
    var value = $('input[name=dd_sel]:checked').val();

    if (value === 'dd_range') {
      if($('tr:has(.dd-hidden)').is(':hidden')) {
        $('tr:has(.dd-hidden)').show()
      } else {
        $('tr:has(.dd-hidden)').hide()
      }
    } else {
      $('tr:has(.dd-hidden)').hide()
    }
  }

  function rdRange() {
    var value = $('input[name=rd_sel]:checked').val()

    if (value === 'rd_range') {
      if($('tr:has(.rd-hidden)').is(':hidden')) {
        $('tr:has(.rd-hidden)').show();
      } else {
        $('tr:has(.rd-hidden)').hide();
      }
    } else {
      $('tr:has(.rd-hidden)').hide();
    }
  }

  $(document).ready(function() { initPage(); });
