  function updateUsers() {      
          $.ajax({
              method: "GET",
              url: "users.txt",
              cache: false
          })
           .done(function( html ){
              $('#Users').html(html);});
  }
  
  function updateDateTime(){
	  var monthNames = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ];
	  var dayNames= ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

	  // Create a newDate() object
	  var newDate = new Date();
  	  $('#Date').html(dayNames[newDate.getDay()] + ", " + newDate.getDate() + ' ' + monthNames[newDate.getMonth()] + ' ' + newDate.getFullYear());

      var seconds = newDate.getSeconds();
      // Add a leading zero to seconds value
      $("#sec").html(( seconds < 10 ? "0" : "" ) + seconds);
	  
      var minutes = newDate.getMinutes();
      // Add a leading zero to the minutes value
      $("#min").html(( minutes < 10 ? "0" : "" ) + minutes);

      var hours = newDate.getHours();
      // Add a leading zero to the hours value
      ampm = (hours > 12) ? " pm" : " am";
      hours = (hours > 12) ? hours - 12 : hours; 
      $("#hours").html(( hours < 10 ? "0" : "" ) + hours);
      $("#ampm").html(ampm);	
  }
  
  function showMessage(){
	  $('#Message').html("Please scan button")
	  $('#Message').fadeTo(500, 1.0); 
  }
  
  function hideName(){
	  $('#Message').fadeTo(1000, 0.1, function(){showMessage()});
  }
     
  $(document).ready(function() {
	  updateDateTime();
      var ws = new WebSocket('ws://octopi.local:9090/ws');
      ws.onmessage = function (evt) {
		  $('#Message').html(evt.data);
		  updateUsers();
		  setTimeout(function(){hideName()}, 5*1000);
      };     
  	  setInterval(function(){updateDateTime()}, 1000);
  });
