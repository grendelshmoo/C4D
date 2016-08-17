  function toggleSearchForm() {
    if ($('.search-field').is(':hidden')){
      $('.search-field').show();
      $('.search-icon').html('[-]');
    } else {
      $('.search-field').hide();
      $('.search-icon').html('[+]');
    }
  }

  function initPage(){
	   $(".search-field").hide();
  }

  $(document).ready(function() { initPage(); });
