<?php
      $myfile = fopen("message.txt", "r") or die("Unable to open file!");
      $read=fread($myfile,filesize("message.txt"));
      fclose($myfile);
      echo $read;
  ?>
