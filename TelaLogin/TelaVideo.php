<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="estilo.css/estilo1.css">
    <title>Visualização</title>
    <h1>Seus vídeos</h1><br>
    <style>
        body{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            min-height: vh;
        }
        video{
            width: 640px;
            height: 360px;
        }
    </style>
</head>
<body>
    <form action="Video.php" method="post">
  
        <div class="alb">
            <?php
            include "config.php";

            if (isset($_SESSION['user_email'])) {
                $loggedInEmail = $_SESSION['user_email'];
                $sql = "SELECT * FROM videos WHERE email = '$loggedInEmail' ORDER BY id DESC";
                $res = mysqli_query($conn, $sql);
                echo"$loggedInEmail";
                if (mysqli_num_rows($res) > 0) {
                    while ($videos = mysqli_fetch_assoc($res)) {
                        ?>
                        <video src="uploads/<?= $videos['video_url'] ?>" controls></video>
                        <?php
                    }
                } else {

                    echo "<h1>Nenhum vídeo encontrado para este usuário.</h1>";
                }
            } else {
                echo "<h1>Faça login para ver os vídeos.</h1>";
            }
            ?>
        </div>
        <input type="submit" name="upload" value="Upload">
        
    </form>
</body>
</html>

