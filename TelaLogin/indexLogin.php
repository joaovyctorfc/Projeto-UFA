<?php
require_once "config.php";
$message = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $senha = $_POST['senha'];

    $sql = "SELECT id, senha FROM usuario WHERE email = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();

        if (password_verify($senha, $row['senha'])) {
            session_start();
            $_SESSION['user_email'] = $email; 
            header("Location: index.php"); 
            exit();
        } else {
            $message = "Senha incorreta.";
        }
   
    } else {
        $message = "Usuário não encontrado.";
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="estilo.css/estilo1.css"> 
</head>
<body>
    <h1>Login</h1><br>
    <?php if (!empty($error)) { echo "<p>$error</p>"; } ?>

    <form method="post" action="indexLogin.php">
        E-mail: <input type="text" name="email" required><br>
        Senha: <input type="password" name="senha" required><br>
        <input type="submit" value="Login">
    </form>
    <br>
    <a href="cadastrar.php">Ainda não é cadastrado?</a>
    <p><?php echo $message; ?></p>

</body>
</html>

