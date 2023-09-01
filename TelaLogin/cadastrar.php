<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="estilo.css/estilo1.css">
</head>
<body>
    <h1> Cadastrar </h1><br> 
    <form method="post" action="cadastrar.php">
        E-mail: <input type="text" name="email" required><br>
        Senha: <input type="password" name="senha" required><br>
        <input type="submit" value="Cadastrar">
    </form>
    <br>
    <a href="indexLogin.php">Faça Login</a>

    <?php
    require_once "config.php";
    $message = ""; 

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $email = $_POST['email'];
        $senha = $_POST['senha'];

        $checkEmailQuery = "SELECT id FROM usuario WHERE email = ?";
        $stmtCheck = $conn->prepare($checkEmailQuery);
        $stmtCheck->bind_param("s", $email);
        $stmtCheck->execute();
        $stmtCheck->store_result();

        if ($stmtCheck->num_rows > 0) {
            $message = "Email já existe.";
        } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $message = "E-mail no formato inválido.";
        } else {
            $hashed_senha = password_hash($senha, PASSWORD_DEFAULT);
            $insertQuery = "INSERT INTO usuario (email, senha) VALUES (?, ?)";
            $stmt = $conn->prepare($insertQuery);
            $stmt->bind_param("ss", $email, $hashed_senha);

            if ($stmt->execute()) {
                $message = "Usuário criado com sucesso.";
            }
        }
    }
    ?>

    <p><?php echo $message; ?></p>

</body>
</html>

