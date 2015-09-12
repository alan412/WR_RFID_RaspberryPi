//TODO: Change so date is also updated.   Combine all date and time into one function
//TODO: Make so the message is only visible for one second

  function updateDisplay() {
          $.ajax({
              method: "GET",
              url: "message.txt",
              cache: false
          })
           .done(function( html ){
              $('#Message').html(html);});
        
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
  	  $('#Date').html(dayNames[newDate.getDay()] + " " + newDate.getDate() + ' ' + monthNames[newDate.getMonth()] + ' ' + newDate.getFullYear());

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
     
  $(document).ready(function() {
	  updateDateTime();
	  updateDisplay(); 
      
  	  setInterval(function(){updateDateTime()}, 1000);
      setInterval(function(){updateDisplay()}, 250);
  });
