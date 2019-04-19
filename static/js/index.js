$(document).ready(function()
{
  $("#changebg").click(function(){
   var imgurl1 = "/static/images/bg"
   var imgurl2 = Math.round(Math.random()*6)
   var imgurl3 = ".jpg"
   var imgurl = imgurl1+imgurl2+imgurl3
   var imgurl ="url("+imgurl+")"
    $("body").css("background-image",imgurl);
    // console.log(imgurl)

  });

});

$(document).ready(function(){
$("#qrimg").click(function(){
  $.get("/qrcode/getimgsrc",function(json){
   $(".img-responsive").attr("src",json.imgsrc)
  })
})
})

$(document).ready(function(){
$("#startbutton").click(function(){
  $.get("/qrcode/getimgsrc",function(json){
   $(".img-responsive").attr("src",json.imgsrc)
  })
})
})


$(document).ready(function(){
$("#clearcache").click(function(){
  $.get("/qrcode/clearcache",function(json){
   $(".img-responsive").attr("src",json.imgsrc)
   alert("缓存已清理")
  })
})
})

$(function (){
    $("[data-toggle='popover']").popover();
});


// })
// })



   // $.get('/user/register_exist/?uname='+$('#user_name').val(),function(data)
   // {
   //  if(data.count!==0){

   //   $('#user_name').next().html('用户名已经存在');
   //   $('#user_name').next().show();
   //   error_name = true;
   //  }



// $(document).ready(function(){
//    $("#qrimg").click(function(){


//    alert(1)
//    var url='http://114.55.6.49:7888/imgserver/AccountManagerTaskInterface';
//    $.ajax({
//      url:url,
//      contentType:"application/json",
//      dataType:'jsonp',
//      processData: false, 
//      type:'get',
//      success:function(data){
//        alert(data.name);
//      },
//      error:function(XMLHttpRequest, textStatus, errorThrown) {
//        alert(XMLHttpRequest.status);
//        alert(XMLHttpRequest.readyState);
//        alert(textStatus);
//      }});


// })

// })