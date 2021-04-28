<?php

session_start();
    
// connect to db
$db = mysqli_connect('localhost', 'root','', 'Test') or die("database not connected"); 

// register users

if(isset($_POST['reg_user']))
{
    $username = mysqli_real_escape_string($db, $_POST['username']); 
    $email = mysqli_real_escape_string($db, $_POST['email']);
    $password_1 = mysqli_real_escape_string($db, $_POST['password']); 

    $password = md5($password_1);
    $query = "INSERT INTO user (username, email, password) VALUES ('$username', '$email', '$password')"; 

    mysqli_query($db, $query); 
}


// Login user

if(isset($_POST['login_user']))
{
    
    $username = $_POST['username']; 
    $password = $_POST['password'];

    $password = md5($password);

    $data = "SELECT * FROM user WHERE username = '$username' AND password = '$password' "; 
    $result = mysqli_query($db, $data); 
    $check = mysqli_fetch_array($result);   
    
    if(isset($check))
    {
        echo "TOP SECRET : Alien has escaped from Area 51";  
    }
    else
    {
        echo "Wrong Credentials";  
    }
}

/*
WRONG WAY OF LOGIN

    $username = $_POST['username']; 
    $password = $_POST['password'];

    $password = md5($password);

    $data = "SELECT * FROM user WHERE username = '$username' AND password = '$password' "; 
    $result = mysqli_query($db, $data); 
    $check = mysqli_fetch_array($result);   
    
    if(isset($check))
    {
        echo "TOP SECRET : Alien has escaped from Area 51";    
    }
    else
    {
        echo "Wrong Credentials";  
    }

*/

//     Malicious String -> ' or 2=2--  

/*
RIGHT WAY OF LOGIN

    $username = mysqli_real_escape_string($db, $_POST['username']); 
    $password = mysqli_real_escape_string($db, $_POST['password']); 

    $password = md5($password); 

    $query = "SELECT * FROM user WHERE username='$username' AND password='$password' "; 
    $results = mysqli_query($db, $query); 

    if(mysqli_num_rows($results))
    {
        echo "TOP SECRET : Alien has escaped from Area 51";  
    }
    else
    {
        echo "Wrong Credentials";  
    }

*/

?>

