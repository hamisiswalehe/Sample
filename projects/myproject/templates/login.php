<?php include("server1.php"); ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Login form</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <div class="header">
      <h2>Login</h2>
    </div>
    <form action="login.php" method="POST">
      <div class="group">
        <label for="">Firstname</label>
        <input type="text" name="Firstname" placeholder="firstname">

      </div>
      <div class="group">
        <label for="">Lastname</label>
        <input type="text" name="Lastname" placeholder="lastname">

      </div>
      <div class="group">
        <label for="">Password</label>
        <input type="password" name="Password" placeholder="password">
      </div>
      <div class="group">
        <button type="submit" name="Login" class="btn">Login</button>
      </div>
      <p>Not yet a member <a href="register.php">sign up</a>
      </p>
</form>

  </body>
</html>
