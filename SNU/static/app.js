$("body").on("click", "label", function(e) {
    var getValue = $(this).attr("for");
    var goToParent = $(this).parents(".select-size");
    var getInputRadio = goToParent.find("input[id = " + getValue + "]");
    console.log(getInputRadio.attr("id"));  
  });
  