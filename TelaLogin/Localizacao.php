
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
    <title>mapa</title>

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
       
      </form>
    </div>
  </div>
</nav>

    <style> 
    #map { height: 300px; width: 50%;}
    </style>
</head>
<body>
    <h1> Sua localização é:</h1>
    <div id="map"></div>
    <?php
    if (isset($_GET['login']) ) {}
    ?>

 


</body>
</html>