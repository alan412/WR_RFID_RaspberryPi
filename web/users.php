<?php
      $myfile = fopen("users.txt", "r") or die("Unable to open file!");
      $read=fread($myfile,filesize("users.txt"));
      fclose($myfile);
      echo $read;
  ?>
