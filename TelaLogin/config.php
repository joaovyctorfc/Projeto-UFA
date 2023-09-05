<?php
session_start();
$servername = "localhost";
$username = "root";
$password = "";
$database = "login";

$conn = new mysqli($servername, $username, "", $database, 3306);

if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

?>