<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

 <!-- Make sure you put this AFTER Leaflet's CSS -->
 <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
 integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
crossorigin=""></script>
    <title>Visualização</title>

    <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
 
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="Localizacao.php">Home</a>

        </li>
        <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="index.php">Sair</a>
        </li>
        <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="TelaVideo.php">Video</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="Video.php">Upload</a>

        </li>
       
      </form>
    </div>
  </div>
</nav>    <style>
      
        video {
            width: 300px;
            height: 400px;
        }
    </style>
</head>
<body>
    <?php
    include "config.php";

    if (isset($_SESSION['user_email'])) {
        $loggedInEmail = $_SESSION['user_email'];
        $sql = "SELECT * FROM videos WHERE email = '$loggedInEmail' ORDER BY id DESC";
        $res = mysqli_query($conn, $sql);
        if (mysqli_num_rows($res) > 0) {
            ?>
            <form action="" method="post">
                <h1>Seus vídeos</h1><br>
                <div class="alb">
                    <?php
                    while ($videos = mysqli_fetch_assoc($res)) {
                        ?>
                        <label>
                            <input type="checkbox" name="selected_videos[]" value="<?= $videos['video_url'] ?>">
                            <video src="uploads/<?= $videos['video_url'] ?>" controls></video>
                        </label>
                        <?php
                    }
                    ?>
                </div>
                <input type="submit" name="download" value="Download">
            </form>
            <script>
                const checkboxes = document.querySelectorAll('input[type="checkbox"]');
                const downloadButton = document.querySelector('input[name="download"]');
                
                downloadButton.addEventListener('click', () => {
                    const selectedVideos = Array.from(checkboxes).filter(checkbox => checkbox.checked);
                    if (selectedVideos.length === 0) {
                        alert('Selecione pelo menos um vídeo para download.');
                    } else {
                        selectedVideos.forEach(video => {
                            const videoUrl = video.value;
                            const link = document.createElement('a');
                            link.href = 'uploads/' + videoUrl;
                            link.download = videoUrl;
                            link.style.display = 'none';
                            document.body.appendChild(link);
                            link.click();
                            document.body.removeChild(link);
                        });
                    }
                });
            </script>
            <?php
        } else {
            echo "<h1>Nenhum vídeo encontrado para este usuário.</h1>";
        }
    } else {
        echo "<h1>Faça login para ver os vídeos.</h1>";
    }
    ?>
 
</body>
</html>

