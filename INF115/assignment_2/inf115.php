<!DOCTYPE html>
<html>

<head>
  <title>INF115 - Assignment 2</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" type="text/css" href="style/style.css">

</head>

<body>
  <!-- DO NOT TOUCH HERE -->
  <h1>INF115 - Compulsory Exercise 2</h1>
  <div class="bgimg-1 w3-display-container w3-opacity-min" id="home">
    <div class="w3-display-middle" style="white-space:nowrap;">
      <span class="w3-center w3-padding-large w3-black w3-xlarge w3-wide w3-animate-opacity"> <span
          class="w3-hide-small">INF</span> 115</span>
    </div>
  </div>
  <!-- ############################################################# -->

  <?php
  /*
  Database configuration
  */

  // Connection parameters
  $host = 'localhost';
  $user = 'root';
  $password = '';
  $db = 'assignment_2';

  // Connect to the database
  $conn = mysqli_connect($host, $user, $password, $db);

  // Connection check
  if (!$conn) {
    exit('Error: Could not connect to the database.');
  }

  // Set the charset
  mysqli_set_charset($conn, 'utf8');
  ?>


  <!-- PROBLEM 4 -->

  <?php
  $message = '';
  if (isset($_POST['submit4'])) {
    $name = $_POST['name4'] ?? '';
    $username = $_POST['username4'] ?? '';
    $email = $_POST['email4'] ?? '';
    $password = $_POST['password4'] ?? '';

    if ($name && $username && $email && $password) {
      $message4 = 'Successful Registration!';
    } else {
      $message4 = 'Please fill out all fields.';
    }
  }

  ?>

  <div class="w3-content w3-container w3-padding-64" id="about">
    <h3 class="w3-center">Problem 4: HTML Form</h3>
    <!-- write your solution here -->
    <form id="registrationForm" method="post" >
      <label for="name4">Name:</label>
      <input type="text" id="name4" name="name4" maxlength="50" required><br><br>

      <label for="username4">Username:</label>
      <input type="text" id="username4" name="username4" pattern="[a-zA-Z0-9]{1,50}" title="Only alphanumeric characters, no spaces" required><br><br>

      <label for="email4">Email:</label>
      <input type="email" id="email4" name="email4" maxlength="50" pattern="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" title="Invalid email format" required><br><br>

      <label for="password">Password:</label>
      <input type="password" id="password4" name="password4" pattern="[a-zA-Z0-9]{1,50}" title="Only alphanumeric characters, no spaces" required><br><br>

      <input type="reset" value="Reset">
      <input type="submit" name='submit4' value="Submit">
    </form>
    <p><?php if (isset($message4)) {echo $message4;}?></p>

  </div>


  <!-- PROBLEM 5 -->

  <?php 
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['submit5'])) {
      $message5 = '';
      $name = mysqli_real_escape_string($conn, $_POST['name5']);
      $username = mysqli_real_escape_string($conn, $_POST['username5']);
      $email = mysqli_real_escape_string($conn, $_POST['email5']);
      $password = mysqli_real_escape_string($conn, $_POST['password5']);
      $registered_date = date('Y-m-d');

      // Hash the password
      $hashed_password = password_hash($password, PASSWORD_DEFAULT);

      // Check if the email and username are unique
      $sql_email = "SELECT * FROM Users WHERE email='$email'";
      $sql_username = "SELECT * FROM Users WHERE username='$username'";
      $result_email = mysqli_query($conn, $sql_email);
      $result_username = mysqli_query($conn, $sql_username);

      // Creating a unique user_id
      $max_user_id_query = "SELECT MAX(user_id) AS max_user_id FROM Users";
      $result = mysqli_query($conn, $max_user_id_query);

      if ($result && $row = mysqli_fetch_assoc($result)) {
        $new_user_id = $row['max_user_id'] + 1;
    }

      if (mysqli_num_rows($result_email) > 0) {
        $message5 = "Error: Email already exists.";
      } elseif (mysqli_num_rows($result_username) > 0) {
        $message5 = "Error: Username already exists.";
      } else {
        // Insert the user data into the Users table
        $sql = "INSERT INTO Users (user_id, name, username, email, password, registered_date) VALUES ('$new_user_id', '$name', '$username', '$email', '$hashed_password', '$registered_date')";
      }
      if (isset($conn) && isset($sql) && mysqli_query($conn, $sql)) {
        $message5 = "Successful Registration!";
      } elseif (!isset($message5)) {
        $message5 = "Error: " . $sql . "<br>" . mysqli_error($conn);
      }
    }
  }

  ?>



  <div class="w3-content w3-container w3-padding-64" id="about">
    <h3 class="w3-center">Problem 5: Insert into Table</h3>
    <!-- write your solution here -->
    <div class="w3-content w3-container w3-padding-64" id="about">
    <h3 class="w3-center">Problem 5: HTML Form</h3>
    <!-- write your solution here -->
    <form id="registrationForm" method="post" >
      <label for="name">Name:</label>
      <input type="text" id="name5" name="name5" maxlength="50" required><br><br>

      <label for="username">Username:</label>
      <input type="text" id="username5" name="username5" pattern="[a-zA-Z0-9]{1,50}" title="Only alphanumeric characters, no spaces" required><br><br>

      <label for="email4">Email:</label>
      <input type="email" id="email4" name="email5" maxlength="50" pattern="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" title="Invalid email format" required><br><br>

      <label for="password">Password:</label>
      <input type="password" id="password5" name="password5" pattern="[a-zA-Z0-9]{1,50}" title="Only alphanumeric characters, no spaces" required><br><br>

      <input type="reset" value="Reset">
      <input type="submit" name='submit5' value="Submit">
    </form>
    <p><?php if (isset($message5)) {echo $message5;}?></p>
  </div>

  
  <!-- PROBLEM 6 -->

  <?php
  $query = "SELECT * FROM Users";
  $result = mysqli_query($conn, $query);
  ?>


  <div class="w3-content w3-container w3-padding-64" id="about">
    <h3 class="w3-center w3-content">Problem 6: Show data</h3>
    <!-- write your solution here -->
    <table border="1">
      <tr>
        <th>Name</th>
        <th>Username</th>
        <th>Email</th>
        <th>Register date</th>
      </tr>
      <?php while($row = mysqli_fetch_assoc($result)) : ?>
        <tr>
          <td><?php echo htmlspecialchars($row['name']); ?></td>
          <td><?php echo htmlspecialchars($row['username']); ?></td>
          <td><?php echo htmlspecialchars($row['email']); ?></td>
          <td><?php echo htmlspecialchars($row['registered_date']); ?></td>
        </tr>
      <?php endwhile; ?>
    </table>
  </div>


  <!-- PROBLEM 7 -->
<!-- PROBLEM 7 -->
<div class="w3-content w3-container w3-padding-64" id="about">
  <h3 class="w3-center">Problem 7: Search data</h3>
  <!-- write your solution here -->
    <form method="post">
      <label for="model">Model:</label>
      <input type="text" id="model" name="model"><br><br>
      
      <label for="category">Category:</label>
      <input type="text" id="category" name="category"><br><br>
      
      <label for="brand">Brand:</label>
      <input type="text" id="brand" name="brand"><br><br>
      
      <input type="submit" name="search" value="Search">
    </form>

    <?php
    if (isset($_POST['search'])) {
      $model = $_POST['model'];
      $category = $_POST['category'];
      $brand = $_POST['brand'];

      $query = "SELECT * FROM Products WHERE model LIKE '%$model%' AND category LIKE '%$category%' AND brand LIKE '%$brand%'";
      $result = mysqli_query($conn, $query);
    ?>

    <table border="1">
      <tr>
        <th>Model</th>
        <th>Category</th>
        <th>Brand</th>
      </tr>
      <?php while($row = mysqli_fetch_assoc($result)) : ?>
        <tr>
          <td><?php echo htmlspecialchars($row['model']); ?></td>
          <td><?php echo htmlspecialchars($row['category']); ?></td>
          <td><?php echo htmlspecialchars($row['brand']); ?></td>
        </tr>
      <?php endwhile; ?>
    </table>
    
    <?php } ?>
  </div>



</body>

</html>