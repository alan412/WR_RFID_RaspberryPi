//TODO: Change so date is also updated.   Combine all date and time into one function
//TODO: Change to not use PHP on the server side
//TODO: Make so the message is only visible for one second

function updateDisplay() {
          var jqxhr = $.get("message.php", function(data){
            $('#Message').html(data);});
          var jqxhr = $.get("users.php", function(data){
            $('#Users').html(data);
      });
  }
   
  $(document).ready(function() {
  // Create two variable with the names of the months and days in an array
  var monthNames = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ];
  var dayNames= ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
   
  // Create a newDate() object
  var newDate = new Date();
  // Extract the current date from Date object
  newDate.setDate(newDate.getDate());
  // Output the day, date, month and year   
  $('#Date').html(dayNames[newDate.getDay()] + " " + newDate.getDate() + ' ' + monthNames[newDate.getMonth()] + ' ' + newDate.getFullYear());
   
  setInterval( function() {
      // Create a newDate() object and extract the seconds of the current time
      var seconds = new Date().getSeconds();
      // Add a leading zero to seconds value
      $("#sec").html(( seconds < 10 ? "0" : "" ) + seconds);
      },1000);
       
  setInterval( function() {
      // Create a newDate() object and extract the minutes of the current time
      var minutes = new Date().getMinutes();
      // Add a leading zero to the minutes value
      $("#min").html(( minutes < 10 ? "0" : "" ) + minutes);
      },1000);
       
  setInterval( function() {
      // Create a newDate() object and extract the hours of the current time
      var hours = new Date().getHours();
      // Add a leading zero to the hours value
      ampm = (hours > 12) ? " pm" : " am";
      hours = (hours > 12) ? hours - 12 : hours; 
      $("#hours").html(( hours < 10 ? "0" : "" ) + hours);
      $("#ampm").html(ampm);
      }, 1000);    
 
  setInterval(function(){updateDisplay()}, 250);
   
  });
