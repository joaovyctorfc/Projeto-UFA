<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Geolocalização</title>
    <link rel="stylesheet" href="estilo.css/estilo3.css">
</head>
<body>
    <h1>Sua localização:<br></h1>
    <h2></h2>
    <?php
    if (isset($_GET['login']) ) {}
    ?>
    <button onclick="voltarParaLogin()">Sair</button>
    <button onclick="CarregarVideo()">Video</button>

    <script src="./script.js"></script>
    <script>
        function voltarParaLogin() {
            window.location.href = "indexlogin.php"; 
        }
        function CarregarVideo() {
            window.location.href = "indexVideo.php"; 
        }
    </script>
</body>
</html>
