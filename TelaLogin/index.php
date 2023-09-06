
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
   integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
   crossorigin=""/>
   <!-- Make sure you put this AFTER Leaflet's CSS -->
 <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
 integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
 crossorigin=""></script>
    <title>mapa</title>

    <style> 
    #map { height: 300px; width: 50%;}
    </style>
</head>
<body>
    <h1> Sua localização é:</h1>
    <h2></h2>
    <div id="map"></div>
    <?php
    if (isset($_GET['login']) ) {}
    ?>
    <button onclick="voltarParaLogin()">Sair</button>
    <button onclick="CarregarVideo()">Video</button>
    <script src="./script.js"></script> 
    <script>
        function voltarParaLogin() {
            window.location.href = "indexLogin.php"; 
        }
        function CarregarVideo() {
            window.location.href = "indexVideo.php"; 
        }
    </script>
</body>
</html>